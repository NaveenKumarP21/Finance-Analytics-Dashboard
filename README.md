# 📊 Finance Analytics Dashboard

An interactive financial data analytics dashboard developed using Python and Dash to transform financial data into meaningful insights through interactive visualizations.

The dashboard processes **5,200 cleaned financial records** and provides multiple perspectives for analyzing companies, sectors, transactions, market trends, and risk.

---

## Project Overview

The Finance Analytics Dashboard provides an interactive environment for exploring and analyzing financial data.

The dashboard combines data preprocessing, exploratory data analysis, financial analysis, and interactive visualization to help users understand financial performance, transaction activity, market trends, and risk-related patterns.

---

## ✨ Features

### Interactive Filters

The dashboard provides interactive filters for:

- Sector
- Region
- Transaction Type
- Year
- Analyst Rating

These filters allow users to dynamically explore different parts of the financial dataset.

### Financial KPIs

The dashboard provides key financial performance indicators including:

- Transactions
- Net Value
- Average Risk
- Buy Rate
- Average P/E
- Companies

### Company & Transaction Analysis

The dashboard provides:

- Top Companies by Net Value
- Transaction Type Distribution
- Company-level financial analysis
- Buy and Sell transaction analysis

### Trend Analysis

Financial trends can be explored through:

- Monthly Net Value Trends
- Yearly Net Value Trends
- Buy vs Sell Transactions Over Time

### Sector & Regional Analysis

The dashboard provides:

- Net Value by Sector
- Transactions by Region
- Average Risk Score by Sector

### Risk & Rating Analysis

The dashboard includes:

- Average Risk Score analysis
- Analyst Rating analysis
- Financial Metrics Correlation Heatmap

### 3D Risk-Return Analysis

An interactive 3D visualization provides analysis using:

- Market Capitalization
- P/E Ratio
- Risk Score
- Return on Equity (ROE)

This provides an additional perspective for understanding relationships between financial performance and risk.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Plotly**
- **Dash**
- **Excel**

---

## 📂 Project Structure

```text
Finance-Analytics-Dashboard/
│
├── app.py
├── finance_dataset.xlsx
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

```text
app.py
   ↓
Main Dash application containing data processing,
dashboard layout, filters, KPIs, and visualizations.

finance_dataset.xlsx
   ↓
Financial dataset used for analysis and visualization.

requirements.txt
   ↓
Python dependencies required to run the project.

README.md
   ↓
Project documentation.

.gitignore
   ↓
Prevents unnecessary local and system files from being uploaded.
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/NaveenKumarP21/Finance-Analytics-Dashboard.git
```

### 2. Navigate to the Project Directory

```bash
cd Finance-Analytics-Dashboard
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run Locally

Start the Dash application using:

```bash
python app.py
```

Once the application starts, open your browser and go to:

```text
http://127.0.0.1:8050
```

The dashboard can then be explored using the available filters, KPI cards, charts, and 3D visualization.

---

## 🔄 How It Works

The dashboard follows a data analytics workflow:

```text
Financial Dataset
       ↓
Data Loading
       ↓
Data Cleaning
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Financial Analysis
       ↓
KPI Calculation
       ↓
Interactive Filtering
       ↓
Data Visualization
       ↓
Financial Insights
```

### Data Analysis Workflow

```text
5,200 Financial Records
          ↓
    Data Processing
          ↓
   Data Preparation
          ↓
 Financial Calculations
          ↓
Interactive Dashboard
          ↓
   Visual Analysis
          ↓
 Financial Insights
```

---

## 📊 Dashboard Components

```text
Interactive Filters
       ↓
Sector | Region | Transaction Type | Year | Analyst Rating
```

```text
Financial KPIs
       ↓
Transactions | Net Value | Average Risk
Buy Rate | Average P/E | Companies
```

```text
Company & Transaction Analysis
       ↓
Top Companies by Net Value
Transaction Type Distribution
```

```text
Trend Analysis
       ↓
Monthly Net Value
Yearly Net Value
Buy vs Sell Transactions
```

```text
Sector & Regional Analysis
       ↓
Net Value by Sector
Transactions by Region
Average Risk Score by Sector
```

```text
Risk & Rating Analysis
       ↓
Analyst Ratings
Risk Analysis
Correlation Heatmap
```

```text
Advanced Analysis
       ↓
3D Risk-Return Visualization
Market Cap | P/E | Risk Score | ROE
```

---

## 📈 Key Analysis Areas

### Company Analysis

Analyze companies based on their financial transaction value and identify companies with higher net value.

### Sector Analysis

Compare financial performance and risk across different sectors.

### Transaction Analysis

Explore transaction types and compare Buy and Sell activity.

### Regional Analysis

Analyze transaction activity across different regions.

### Time-Based Analysis

Explore monthly and yearly changes in financial net value.

### Risk Analysis

Analyze risk scores across sectors and examine relationships between financial metrics.

### Analyst Rating Analysis

Explore the distribution and impact of analyst ratings within the financial dataset.

### Correlation Analysis

Use a correlation heatmap to understand relationships between different financial metrics.

### Risk-Return Analysis

Use the interactive 3D visualization to explore relationships between Market Capitalization, P/E Ratio, Risk Score, and ROE.

---

## 📦 Requirements

The project uses the following Python packages:

```text
dash>=2.17.0
plotly>=5.20.0
pandas>=2.1.0
numpy>=1.26.0
openpyxl>=3.1.0
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Project Purpose

This project was developed to strengthen practical skills in:

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Financial Data Analysis
- Data Visualization
- Interactive Dashboard Development
- Python Programming

The project also provided practical experience in presenting complex financial datasets through an interactive and user-friendly dashboard.

---

## 🔮 Future Enhancements

- Integration with real-time financial market data
- Machine learning-based financial risk prediction
- Advanced predictive analytics
- Portfolio performance analysis
- Additional financial indicators
- Deployment as a web application
- Improved responsive dashboard experience

---

## 👨‍💻 Author

### Naveen Kumar P

Computer Science Engineering Student

Interested in Software Development, Data Analytics, Data Science, and building practical applications using modern technologies.

---

## 📄 License

This project is intended for **educational and portfolio purposes**.