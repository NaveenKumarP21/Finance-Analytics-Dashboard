import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# ---------------------------------------------------------------------------
# 1. DATA LOADING & CLEANING
# ---------------------------------------------------------------------------
DATA_FILE = os.path.join(os.path.dirname(__file__), "finance_dataset.xlsx")

NUM_COLS = [
    "Price", "Quantity", "Total_Value", "Commission", "Tax_Rate", "Net_Value",
    "Market_Cap", "PE_Ratio", "EPS", "Dividend_Yield", "Beta", "Revenue",
    "Profit_Margin", "Debt_to_Equity", "ROA", "ROE", "Volume",
    "High_52W", "Low_52W", "Risk_Score",
]
CAT_COLS = ["Company", "Sector", "Region", "Transaction_Type",
            "Currency", "Analyst_Rating"]


def load_and_clean(path: str = DATA_FILE):
    """Load the Excel file and run full cleaning pipeline."""
    df = pd.read_excel(path, sheet_name="Finance Data")
    raw_n = len(df)

    # Remove duplicates
    df = df.drop_duplicates().reset_index(drop=True)
    dups = raw_n - len(df)

    # Fix data types
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for c in NUM_COLS:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Impute nulls (median for numeric, mode for categorical)
    nulls = int(df[NUM_COLS + CAT_COLS].isna().sum().sum())
    for c in NUM_COLS:
        df[c] = df[c].fillna(df[c].median())
    for c in CAT_COLS:
        mode_val = df[c].mode().iloc[0] if not df[c].mode().empty else "Unknown"
        df[c] = df[c].fillna(mode_val)
    df["Date"] = df["Date"].fillna(df["Date"].median())

    # Feature engineering
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
    df["Is_Buy"] = df["Analyst_Rating"].isin(["Buy", "Strong Buy"]).astype(int)
    df["Is_HighRisk"] = (df["Risk_Score"] >= 7).astype(int)

    return df, {"raw": raw_n, "dups": dups, "nulls": nulls, "final": len(df)}


DF, STATS = load_and_clean()

# ---------------------------------------------------------------------------
# 2. STYLING (dark analytics theme)
# ---------------------------------------------------------------------------
COLORS = {
    "bg": "#0b1220",
    "panel": "#111a2e",
    "panel2": "#0f1626",
    "border": "#1e2a44",
    "text": "#e6edf7",
    "muted": "#94a3b8",
    "primary": "#38bdf8",
    "good": "#4ade80",
    "bad": "#f87171",
    "warn": "#fbbf24",
}

SEQ = ["#38bdf8", "#f472b6", "#4ade80", "#fbbf24",
       "#a78bfa", "#f87171", "#22d3ee", "#fb923c"]


def base_layout(**kwargs):
    """Common Plotly layout for a dark, transparent panel."""
    layout = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=COLORS["text"], family="Inter, system-ui, sans-serif"),
        margin=dict(l=50, r=20, t=30, b=50),
        legend=dict(bgcolor="rgba(0,0,0,0)", orientation="h", y=-0.2),
        xaxis=dict(gridcolor="rgba(148,163,184,0.15)"),
        yaxis=dict(gridcolor="rgba(148,163,184,0.15)"),
    )
    layout.update(kwargs)
    return layout


def fmt_money(n):
    if n is None or pd.isna(n):
        return "—"
    n = float(n)
    for unit, div in [("T", 1e12), ("B", 1e9), ("M", 1e6), ("K", 1e3)]:
        if abs(n) >= div:
            return f"${n/div:,.2f}{unit}"
    return f"${n:,.2f}"


# ---------------------------------------------------------------------------
# 3. REUSABLE UI COMPONENTS
# ---------------------------------------------------------------------------
def kpi_card(label, value, accent="primary", icon=""):
    return html.Div(
        style={
            "background": COLORS["panel"],
            "borderLeft": f"4px solid {COLORS[accent]}",
            "borderRadius": "12px",
            "padding": "18px 20px",
            "boxShadow": "0 4px 20px rgba(0,0,0,0.3)",
        },
        children=[
            html.Div(
                style={"display": "flex", "justifyContent": "space-between"},
                children=[
                    html.P(label.upper(),
                           style={"fontSize": "11px", "letterSpacing": "2px",
                                  "color": COLORS["muted"], "margin": 0}),
                    html.Span(icon, style={"color": COLORS["muted"]}),
                ],
            ),
            html.P(value, style={"fontSize": "28px", "fontWeight": 700,
                                 "color": COLORS["text"], "margin": "8px 0 0"}),
        ],
    )


def chart_panel(title, fig, height=380):
    fig.update_layout(height=height)
    return html.Div(
        style={
            "background": COLORS["panel"],
            "border": f"1px solid {COLORS['border']}",
            "borderRadius": "12px",
            "padding": "16px",
            "boxShadow": "0 4px 20px rgba(0,0,0,0.3)",
        },
        children=[
            html.H3(title, style={"fontSize": "14px", "fontWeight": 600,
                                  "color": COLORS["text"], "margin": "0 0 10px"}),
            dcc.Graph(figure=fig, 
                      config={"displaylogo": False}, 
                      style={"width":"100%","height":f"{height}px"}),
        ],
    )


def dropdown(id_, options, placeholder):
    return dcc.Dropdown(
        id=id_,
        options=[{"label": str(o), "value": o} for o in options],
        multi=True,
        placeholder=placeholder,
        style={"background": COLORS["panel2"], "color": "#000",
               "borderRadius": "8px"},
    )


# ---------------------------------------------------------------------------
# 4. APP LAYOUT
# ---------------------------------------------------------------------------
app = Dash(__name__, title="Finance Analytics Dashboard")
server = app.server  # for deployment

sectors = sorted(DF["Sector"].unique())
regions = sorted(DF["Region"].unique())
types_ = sorted(DF["Transaction_Type"].unique())
years = sorted(DF["Year"].unique())
ratings = sorted(DF["Analyst_Rating"].unique())

app.layout = html.Div(
    style={"background": f"linear-gradient(135deg,{COLORS['bg']},#101a33)",
           "minHeight": "100vh", "color": COLORS["text"],
           "fontFamily": "Inter, system-ui, sans-serif", "padding": "24px"},
    children=[
        # Header
        html.Div(
            style={"display": "flex", "justifyContent": "space-between",
                   "alignItems": "flex-end", "flexWrap": "wrap",
                   "marginBottom": "20px"},
            children=[
                html.Div([
                    html.H1("Finance Analytics Dashboard",
                            style={"margin": 0, "fontSize": "32px",
                                   "background": "linear-gradient(90deg,#38bdf8,#a78bfa,#38bdf8)",
                                   "WebkitBackgroundClip": "text",
                                   "WebkitTextFillColor": "transparent"}),
                    html.P("Interactive insights across companies, sectors, and risk",
                           style={"color": COLORS["muted"], "margin": "4px 0 0"}),
                ]),
                html.Div([
                    html.Div(f"{len(DF):,} cleaned records",
                             style={"color": COLORS["primary"], "fontWeight": 600}),
                    html.Div(f"Removed {STATS['dups']} duplicates · imputed {STATS['nulls']} nulls",
                             style={"color": COLORS["muted"], "fontSize": "12px"}),
                ]),
            ],
        ),

        # Filters
        html.Div(
            style={"background": COLORS["panel"], "borderRadius": "12px",
                   "padding": "16px", "marginBottom": "20px"},
            children=[
                html.P("FILTERS", style={"fontSize": "11px", "letterSpacing": "2px",
                                         "color": COLORS["muted"], "margin": "0 0 10px"}),
                html.Div(
                    style={"display": "grid",
                           "gridTemplateColumns": "repeat(5, 1fr))",
                           "gap": "10px"},
                    children=[
                        dropdown("f-sector", sectors, "Sector"),
                        dropdown("f-region", regions, "Region"),
                        dropdown("f-type", types_, "Transaction Type"),
                        dropdown("f-year", years, "Year"),
                        dropdown("f-rating", ratings, "Analyst Rating"),
                    ],
                ),
            ],
        ),

        # KPI cards
        html.Div(id="kpi-row",
                 style={"display": "grid",
                        "gridTemplateColumns": "repeat(auto-fit, minmax(180px, 1fr))",
                        "gap": "14px", "marginBottom": "20px"}),

        # Chart grids
        html.Div(id="charts-row1",
                 style={"display": "grid",
                        "gridTemplateColumns": "repeat(2, minmax(0, 1fr))",
                        "gap": "16px", "marginBottom": "16px"}),
        html.Div(id="charts-row2",
                 style={"display": "grid",
                        "gridTemplateColumns": "repeat(2, minmax(0, 1fr))",
                        "gap": "16px", "marginBottom": "16px"}),
        html.Div(id="charts-row3",
                 style={"display": "grid",
                        "gridTemplateColumns": "repeat(2, minmax(0, 1fr))",
                        "gap": "16px", "marginBottom": "16px"}),
        html.Div(id="charts-row4",
                 style={"display": "grid",
                        "gridTemplateColumns": "repeat(2, minmax(0, 1fr))",
                        "gap": "16px", "marginBottom": "16px"}),

        html.H2("Market Activity Trends",
                style={"fontSize": "20px", "marginTop": "24px"}),
        html.Div(id="charts-row5",
                 style={"display": "grid",
                        "gridTemplateColumns": "repeat(2, minmax(0, 1fr))",
                        "gap": "16px", "marginBottom": "16px"}),

        html.H2("3D Risk-Return View",
                style={"fontSize": "20px", "marginTop": "24px"}),
        html.Div(id="charts-row6", style={"marginBottom": "20px"}),

        html.Footer(
            f"Built with Plotly Dash · {STATS['final']:,} cleaned records",
            style={"textAlign": "center", "color": COLORS["muted"],
                   "fontSize": "12px", "padding": "20px"},
        ),
    ],
)


# ---------------------------------------------------------------------------
# 5. CALLBACK — update everything from filters
# ---------------------------------------------------------------------------
@app.callback(
    Output("kpi-row", "children"),
    Output("charts-row1", "children"),
    Output("charts-row2", "children"),
    Output("charts-row3", "children"),
    Output("charts-row4", "children"),
    Output("charts-row5", "children"),
    Output("charts-row6", "children"),
    Input("f-sector", "value"),
    Input("f-region", "value"),
    Input("f-type", "value"),
    Input("f-year", "value"),
    Input("f-rating", "value"),
)
def update(sector, region, type_, year, rating):
    df = DF.copy()
    if sector:  df = df[df["Sector"].isin(sector)]
    if region:  df = df[df["Region"].isin(region)]
    if type_:   df = df[df["Transaction_Type"].isin(type_)]
    if year:    df = df[df["Year"].isin(year)]
    if rating:  df = df[df["Analyst_Rating"].isin(rating)]

    if df.empty:
        empty = html.Div("No data for current filters.",
                         style={"color": COLORS["muted"], "padding": "40px",
                                "textAlign": "center"})
        return [empty], [], [], [], [], [], []

    # ----- KPIs -----
    total = len(df)
    net_value = df["Net_Value"].sum()
    avg_risk = df["Risk_Score"].mean()
    avg_pe = df["PE_Ratio"].mean()
    buy_rate = df["Is_Buy"].mean() * 100
    n_companies = df["Company"].nunique()

    kpis = [
        kpi_card("Transactions", f"{total:,}", "primary", "📊"),
        kpi_card("Net Value", fmt_money(net_value), "good", "💰"),
        kpi_card("Avg Risk", f"{avg_risk:.2f} / 10", "bad", "⚠️"),
        kpi_card("Buy Rate", f"{buy_rate:.1f}%", "warn", "📈"),
        kpi_card("Avg P/E", f"{avg_pe:.1f}", "primary", "🎯"),
        kpi_card("Companies", f"{n_companies}", "good", "🏢"),
    ]

    # ----- Row 1: Top companies + Tx type pie -----
    top_co = (df.groupby("Company")["Net_Value"].sum()
              .sort_values(ascending=False).head(12).reset_index())
    fig_top = go.Figure(go.Bar(
        x=top_co["Net_Value"], y=top_co["Company"], orientation="h",
        marker=dict(color=top_co["Net_Value"], colorscale="Tealgrn"),
        hovertemplate="%{y}<br>Net Value: $%{x:,.0f}<extra></extra>",
    ))
    fig_top.update_layout(**base_layout(yaxis=dict(autorange="reversed",
                                                   gridcolor="rgba(148,163,184,0.15)")))

    tx = df["Transaction_Type"].value_counts().reset_index()
    tx.columns = ["Type", "Count"]
    fig_tx = go.Figure(go.Pie(labels=tx["Type"], values=tx["Count"], hole=0.55,
                              marker=dict(colors=SEQ), textinfo="label+percent"))
    fig_tx.update_layout(**base_layout())

    row1 = [chart_panel("Top Companies by Net Value", fig_top),
            chart_panel("Transaction Type Distribution", fig_tx)]

    # ----- Row 2: Monthly + Yearly value -----
    mv = df.groupby("YearMonth")["Net_Value"].sum().reset_index().sort_values("YearMonth")
    fig_mv = go.Figure(go.Scatter(x=mv["YearMonth"], y=mv["Net_Value"],
                                  mode="lines+markers", fill="tozeroy",
                                  line=dict(color=COLORS["primary"], width=3)))
    fig_mv.update_layout(**base_layout())

    yv = df.groupby("Year")["Net_Value"].sum().reset_index()
    fig_yv = go.Figure(go.Bar(x=yv["Year"], y=yv["Net_Value"],
                              marker_color=COLORS["good"]))
    fig_yv.update_layout(**base_layout())

    row2 = [chart_panel("Net Value Over Time (Monthly)", fig_mv),
            chart_panel("Yearly Net Value", fig_yv)]

    # ----- Row 3: Sector value bar + Region pie -----
    sv = df.groupby("Sector")["Net_Value"].sum().sort_values(ascending=False).reset_index()
    fig_sv = go.Figure(go.Bar(x=sv["Sector"], y=sv["Net_Value"],
                              marker=dict(color=sv["Net_Value"], colorscale="Viridis")))
    fig_sv.update_layout(**base_layout(xaxis=dict(tickangle=-25,
                                                   gridcolor="rgba(148,163,184,0.15)")))

    rg = df["Region"].value_counts().reset_index()
    rg.columns = ["Region", "Count"]
    fig_rg = go.Figure(go.Pie(labels=rg["Region"], values=rg["Count"],
                              marker=dict(colors=SEQ), textinfo="label+percent"))
    fig_rg.update_layout(**base_layout())

    row3 = [chart_panel("Net Value by Sector", fig_sv),
            chart_panel("Transactions by Region", fig_rg)]

    # ----- Row 4: Risk by sector + Analyst ratings -----
    rs = df.groupby("Sector")["Risk_Score"].mean().sort_values(ascending=False).reset_index()
    fig_rs = go.Figure(go.Bar(x=rs["Risk_Score"], y=rs["Sector"], orientation="h",
                              marker=dict(color=rs["Risk_Score"], colorscale="Reds")))
    fig_rs.update_layout(**base_layout(yaxis=dict(autorange="reversed",
                                                   gridcolor="rgba(148,163,184,0.15)")))

    ar = df["Analyst_Rating"].value_counts().reset_index()
    ar.columns = ["Rating", "Count"]
    fig_ar = go.Figure(go.Bar(x=ar["Rating"], y=ar["Count"],
                              marker_color=SEQ[:len(ar)]))
    fig_ar.update_layout(**base_layout())

    row4 = [chart_panel("Average Risk Score by Sector", fig_rs),
            chart_panel("Analyst Ratings", fig_ar)]

    # ----- Row 5: Correlation heatmap + Buy/Sell trend -----
    corr_cols = ["Price", "Net_Value", "Market_Cap", "PE_Ratio", "EPS",
                 "Dividend_Yield", "Beta", "Profit_Margin", "ROA", "ROE", "Risk_Score"]
    corr = df[corr_cols].corr().round(2)
    fig_corr = go.Figure(go.Heatmap(z=corr.values, x=corr_cols, y=corr_cols,
                                    colorscale="RdBu", reversescale=True,
                                    zmin=-1, zmax=1,
                                    hovertemplate="%{x} × %{y}: %{z}<extra></extra>"))
    fig_corr.update_layout(**base_layout(xaxis=dict(tickangle=-30)))

    buy = (df[df["Transaction_Type"] == "Buy"].groupby("YearMonth").size()
           .reset_index(name="n").sort_values("YearMonth"))
    sell = (df[df["Transaction_Type"] == "Sell"].groupby("YearMonth").size()
            .reset_index(name="n").sort_values("YearMonth"))
    fig_bs = go.Figure()
    fig_bs.add_trace(go.Scatter(x=buy["YearMonth"], y=buy["n"], mode="lines",
                                name="Buy", line=dict(color=COLORS["good"], width=2)))
    fig_bs.add_trace(go.Scatter(x=sell["YearMonth"], y=sell["n"], mode="lines",
                                name="Sell", line=dict(color=COLORS["bad"], width=2)))
    fig_bs.update_layout(**base_layout())

    row5 = [chart_panel("Correlation Heatmap (Financial Metrics)", fig_corr),
            chart_panel("Buy vs Sell Transactions Over Time", fig_bs)]

    # ----- Row 6: 3D scatter -----
    sample = df.sample(min(1500, len(df)), random_state=42)
    fig_3d = go.Figure(go.Scatter3d(
        x=sample["Market_Cap"], y=sample["PE_Ratio"], z=sample["Risk_Score"],
        mode="markers",
        text=sample["Company"] + " (" + sample["Sector"] + ")",
        hovertemplate="%{text}<br>MCap: $%{x:,.0f}<br>P/E: %{y}<br>Risk: %{z}<extra></extra>",
        marker=dict(size=3, color=sample["ROE"], colorscale="Viridis",
                    opacity=0.75, colorbar=dict(title="ROE")),
    ))
    fig_3d.update_layout(**base_layout(
        scene=dict(
            xaxis=dict(title="Market Cap (log)", type="log",
                       color=COLORS["text"], gridcolor="rgba(148,163,184,0.2)"),
            yaxis=dict(title="P/E Ratio", color=COLORS["text"],
                       gridcolor="rgba(148,163,184,0.2)"),
            zaxis=dict(title="Risk Score", color=COLORS["text"],
                       gridcolor="rgba(148,163,184,0.2)"),
            bgcolor="rgba(0,0,0,0)",
        ),
    ))
    row6 = [chart_panel("3D View: Market Cap × P/E × Risk Score (colored by ROE)",
                        fig_3d, height=560)]

    return kpis, row1, row2, row3, row4, row5, row6


# ---------------------------------------------------------------------------
# 6. ENTRY POINT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print(f"✅ Loaded {STATS['final']:,} rows "
          f"(removed {STATS['dups']} dupes, imputed {STATS['nulls']} nulls)")
    print("🚀 Open http://127.0.0.1:8050")
    app.run(debug=True, host="127.0.0.1", port=8050)
