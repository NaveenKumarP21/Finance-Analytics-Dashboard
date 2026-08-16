# 📊 Finance Analytics Dashboard

An interactive financial data analytics dashboard built with **Python, Pandas, NumPy, Plotly, and Dash** to explore companies, sectors, transactions, financial metrics, risk, and market activity through interactive visualizations.

---

## Project Overview

The **Finance Analytics Dashboard** transforms financial transaction data into an interactive analytics experience.

The application loads financial data from an Excel dataset, performs data cleaning and preprocessing, creates analytical features, calculates key financial indicators, and presents the results through interactive charts and a 3D visualization.

The dashboard allows users to explore financial data using interactive filters, KPI cards, and visual analytics.

---

## ✨ Features

### Interactive Dashboard

- Interactive financial analytics dashboard
- Dark-themed dashboard interface
- Interactive charts and visualizations
- Dynamic filtering of financial data

### Data Processing

- Loads financial data from an Excel dataset
- Removes duplicate records
- Handles missing values using median and mode imputation
- Processes date-related information
- Creates Year, Month, and YearMonth features
- Generates risk-related features and flags

### Interactive Filters

The dashboard provides filters for:

- Sector
- Region
- Transaction Type
- Year
- Analyst Rating

### Key Performance Indicators

The dashboard displays:

- Transactions
- Net Value
- Average Risk
- Buy Rate
- Average P/E
- Companies

### Financial Visualizations

The dashboard includes:

- Top Companies by Net Value
- Transaction Type Distribution
- Monthly Net Value Trends
- Yearly Net Value
- Net Value by Sector
- Transactions by Region
- Average Risk Score by Sector
- Analyst Ratings
- Financial Metrics Correlation Heatmap
- Buy vs Sell Transactions Over Time

### 3D Risk-Return Analysis

An interactive 3D visualization explores relationships between:

- Market Capitalization
- P/E Ratio
- Risk Score
- ROE

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Plotly**
- **Plotly Dash**
- **OpenPyXL**
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
KPIs, filters, and visualizations.

finance_dataset.xlsx
   ↓
Financial dataset used by the dashboard.

requirements.txt
   ↓
Required Python dependencies.

README.md
   ↓
Project documentation.

.gitignore
   ↓
Prevents unnecessary local and system files from being pushed to GitHub.
```

---

## Installation

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

After installing the required dependencies, start the Dash application:

```bash
python app.py
```

The application will start on your local machine.

Open the following address in your browser:

```text
http://127.0.0.1:8050
```

You can then interact with the dashboard using the available filters, KPI cards, financial charts, and 3D Risk-Return visualization.

> **Note:** The project currently runs locally using Plotly Dash. The `127.0.0.1:8050` address is accessible only from the machine running the application.

---

## How It Works

The application follows this data analytics workflow:

```text
Financial Excel Dataset
        ↓
   Data Loading
        ↓
   Data Cleaning
        ↓
Duplicate Removal
        ↓
Missing Value Handling
        ↓
 Feature Engineering
        ↓
 KPI Calculation
        ↓
Interactive Filtering
        ↓
Data Visualization
        ↓
Financial Insights
```

### Data Processing

The application:

1. Loads the financial dataset from Excel.
2. Removes duplicate records.
3. Handles missing values using median and mode imputation.
4. Processes date-related information.
5. Creates Year, Month, and YearMonth features.
6. Generates risk-related features.
7. Calculates financial KPIs.
8. Displays the processed data through interactive visualizations.

---

## Dashboard Components

```text
KPI Cards
   ↓
Display important financial metrics
```

```text
Sector Filter
   ↓
Analyze specific sectors
```

```text
Region Filter
   ↓
Analyze specific regions
```

```text
Transaction Type Filter
   ↓
Filter transaction types
```

```text
Year Filter
   ↓
Analyze financial activity by year
```

```text
Analyst Rating Filter
   ↓
Explore analyst rating data
```

```text
Interactive Charts
   ↓
Explore financial trends and patterns
```

```text
Correlation Heatmap
   ↓
Explore relationships between financial metrics
```

```text
3D Risk-Return Visualization
   ↓
Analyze Market Cap, P/E, Risk Score, and ROE
```

---

## Key Analytics

### Company Analysis

Compare companies based on their net value and identify companies with higher overall transaction value.

### Sector Analysis

Explore net value and average risk across different sectors.

### Regional Analysis

Analyze transaction distribution across different regions.

### Time-Based Analysis

Study changes in net value and transaction activity across months and years.

### Risk Analysis

Compare risk scores across sectors and explore relationships between financial metrics.

### Transaction Analysis

Analyze transaction types and compare Buy and Sell activity over time.

### Analyst Ratings

Explore the distribution of analyst ratings across the dataset.

---

## Requirements

The project requires the following Python packages:

```text
dash>=2.17.0
plotly>=5.20.0
pandas>=2.1.0
numpy>=1.26.0
openpyxl>=3.1.0
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Future Enhancements

- Integration with real-time financial market data
- Machine learning-based risk prediction
- Advanced predictive analytics
- Portfolio performance analysis
- Additional financial indicators
- Deployment as a public web application
- Improved responsive dashboard experience

---

## Project Purpose

This project was developed to demonstrate practical skills in:

```text
Data Cleaning
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Financial Data Analysis
      ↓
Data Visualization
      ↓
Interactive Dashboard Development
      ↓
Python Programming
      ↓
Data-Driven Application Development
```

---

## 👨‍💻 Author

### Naveen Kumar P

**Computer Science Engineering Student**

Interested in Software Development, Data Analytics, Data Science, and building practical applications using modern technologies.

---

## 📄 License

This project is intended for **educational and portfolio purposes**.