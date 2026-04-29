# Financial Transactions Fraud Detection & Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458.svg)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

An end-to-end data analysis and data engineering pipeline for detecting fraudulent behavior across 1 million financial transactions. This project encompasses comprehensive ETL processes, exploratory data analysis (EDA), statistical modeling, network analysis, and interactive Tableau visualizations.

---

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Project Objectives](#project-objectives)
3. [Dataset Overview](#dataset-overview)
4. [Methodology & Pipeline](#methodology--pipeline)
5. [Key Insights & Findings](#key-insights--findings)
6. [Tech Stack](#tech-stack)
7. [Repository Structure](#repository-structure)
8. [Getting Started](#getting-started)
9. [Future Work](#future-work)

---

## Executive Summary
Financial fraud poses a significant threat to digital banking, resulting in substantial losses through unauthorized transactions. This project analyzes a comprehensive dataset of **1,000,000 transactions** across **50,000 accounts** spanning a three-year period (2022–2024). Through rigorous data processing, feature engineering, and statistical analysis, we successfully identified critical fraud patterns, developed account risk indicators, and isolated **$12.52M** in fraudulent activities, which accounted for **1.71%** of the total transaction volume.

## Project Objectives
- **Data Engineering:** Architect a robust ETL (Extract, Transform, Load) pipeline to clean and transform raw datasets into structured, analytical-ready features.
- **Exploratory Data Analysis (EDA):** Uncover hidden trends, temporal patterns, and geographic distributions of anomalous activities.
- **Statistical Modeling & Risk Scoring:** Develop account-level risk profiles and pinpoint high-risk merchant categories.
- **Network Analysis:** Detect organized fraud rings through shared identifiers (IP addresses, devices, emails).
- **Data Visualization:** Create an intuitive, high-impact Tableau dashboard allowing stakeholders to monitor KPIs and fraud metrics interactively.

---

## Dataset Overview
The analysis leverages five relational datasets, meticulously processed and linked to provide a holistic view of user behavior:

| File | Rows | Description |
|---|---|---|
| `transactions.csv` | 1,000,000 | Individual transaction records (amounts, categories, velocity, target label) |
| `account_profiles.csv` | 50,000 | Account-level aggregates, historical risk scores, and 2FA status |
| `fraud_patterns.csv` | 7 | Categorical lookup table detailing specific fraud types and aggregate statistics |
| `network_edges.csv` | 7,411 | Account-to-account linkages used for fraud-ring and collusive behavior detection |
| `time_series_stats.csv` | 26,280 | Hourly transaction and fraud metrics over a 3-year period |

*Note: Due to file size constraints, `transactions.csv` is tracked via Git LFS.*
**Detailed schema definitions can be found in [docs/data_dictionary.md](docs/data_dictionary.md).**

---

## Methodology & Pipeline

The project strictly follows a structured data science lifecycle:

```text
Raw Data ➔ ETL Pipeline ➔ Feature Engineering ➔ EDA & Statistical Analysis ➔ Dashboarding
```

1. **Extraction:** Loading and inspecting raw CSVs to identify structural issues and missing data.
2. **Transformation (`scripts/etl_pipeline.py`):**
   - Datetime parsing and timezone alignment.
   - Type casting, deduplication, and Boolean standardization.
   - Engineering temporal features (hour, day of week, weekend flags).
   - Calculating behavioral features (transaction velocity, amount-to-average ratios).
3. **Exploratory Analysis (`notebooks/`):** Deep dive into variable distributions, bivariate relationships, correlation matrices, and outlier detection.
4. **Network Analysis:** Graphing connected accounts to flag coordinated fraud rings.
5. **Loading:** Exporting clean, finalized datasets to `data/processed/` for Tableau ingestion and future Machine Learning model training.

---

## Key Insights & Findings

Extensive exploratory and statistical analysis yielded the following critical business insights:

- **Primary Attack Vector:** **Card Not Present (CNP)** transactions represent the most common fraud type, accounting for **34.9%** of all fraudulent activities.
- **Financial Impact Discrepancy:** The average fraudulent transaction is significantly higher (**$730**) compared to legitimate transactions (**$174**), indicating targeted high-value attacks.
- **High-Risk Categories:** The `crypto` (5.3% fraud rate) and `money_transfer` (4.1% fraud rate) merchant categories exhibit the highest susceptibility to fraud.
- **Temporal Vulnerability:** Fraudsters are disproportionately active during off-hours, with approximately **40%** of fraud occurring between **midnight and 5 AM**.
- **Security Posture Vulnerabilities:** Accounts lacking Two-Factor Authentication (2FA) are highly targeted, representing **~40%** of total fraud cases despite making up a smaller portion of the user base.

---

## Tech Stack

- **Data Engineering & Processing:** `Python`, `Pandas`, `NumPy`
- **Exploratory Analysis & Stats:** `Jupyter Notebooks`, `SciPy`
- **Data Visualization:** `Matplotlib`, `Seaborn`, `Plotly`, `Tableau`
- **Version Control:** `Git`, `Git LFS`
- **Web Portfolio:** `React 19`, `Vite 8`, `GitHub Pages`

---

## Repository Structure

```text
.
├── data/
│   ├── raw/                  # Original CSV files (transactions tracked via Git LFS)
│   └── processed/            # Cleaned data outputs from the ETL pipeline
├── notebooks/                # Step-by-step Jupyter notebooks detailing the analysis
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
├── scripts/                  # Modular Python scripts orchestrating the data pipeline
│   ├── etl_pipeline.py       # Main orchestrator script
│   ├── preprocess.py         # Parsing, null handling, and type casting
│   ├── feature_engineering.py# Temporal and velocity feature creation
│   └── utils.py              # I/O helper functions
├── docs/                     # Documentation including full data dictionaries
├── reports/                  # Project reports, presentation outlines, and templates
├── tableau/                  # Tableau workbook files and dashboard screenshots
├── DVA-focused-Portfolio/    # Source code for the DVA portfolio web application
├── DVA-oriented-Resume/      # Resume assets and related files
└── requirements.txt          # Python project dependencies
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- Git Large File Storage (LFS)

### Installation

1. **Clone the repository and pull large files:**
   ```bash
   git clone https://github.com/AnanyaSoni2004/Global_Stock_Market_AnalysisDashboard
   cd Global_Stock_Market_AnalysisDashboard
   
   # Git LFS is required for the large transactions.csv dataset
   git lfs install
   git lfs pull
   ```

2. **Set up a virtual environment (optional but highly recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the ETL Pipeline:**
   Execute the pipeline to process raw data and generate the finalized datasets.
   ```bash
   python -m scripts.etl_pipeline
   ```

5. **Launch Jupyter Notebooks for Interactive Analysis:**
   ```bash
   jupyter notebook
   ```

---

## Future Work
- **Predictive Machine Learning Integration:** Train and deploy classification models (e.g., Random Forest, XGBoost) using the engineered features to identify fraudulent transactions in real-time.
- **Deep Graph Analysis:** Utilize advanced Graph Neural Networks (GNNs) on `network_edges.csv` to improve the detection rate of sophisticated, multi-node fraud rings.
- **Real-Time Streaming Architecture:** Migrate the current batch ETL pipeline to a streaming architecture utilizing Apache Kafka and PySpark for continuous, low-latency fraud monitoring.
