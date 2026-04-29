# Global Stock Market Analysis — Transactions Fraud Detection

End-to-end fraud detection project on 1 million financial transactions. Covers data engineering, exploratory analysis, statistical modelling, Tableau visualisation, and a DVA-focused portfolio site.

---

## Overview

| Item | Detail |
|---|---|
| Dataset size | 1,000,000 transactions · 50,000 accounts |
| Fraud rate | 1.71 % (17,143 fraudulent transactions) |
| Total fraud losses | $12.52 M |
| Time period | 2022 – 2024 (hourly granularity) |


---

## Repository Structure

```
├── data/
│   ├── raw/                  # Original CSVs (transactions tracked via Git LFS)
│   └── processed/            # Cleaned outputs from the ETL pipeline
├── notebooks/
│   ├── 01_extraction.ipynb   # Data loading and initial inspection
│   ├── 02_cleaning.ipynb     # Missing values, type casting, deduplication
│   ├── 03_eda.ipynb          # Exploratory data analysis
│   ├── 04_statistical_analysis.ipynb  # Fraud pattern and risk analysis
│   └── 05_final_load_prep.ipynb       # Final dataset prep for Tableau / ML
├── scripts/
│   ├── etl_pipeline.py       # Extract → Transform → Load orchestrator
│   ├── preprocess.py         # Datetime parsing, nulls, booleans
│   ├── feature_engineering.py# Date features, velocity, ratio features
│   └── utils.py              # CSV load/save helpers
├── docs/
│   └── data_dictionary.md    # Full schema for all 5 datasets
├── reports/                  # Presentation outline and report template
├── tableau/                  # Dashboard screenshots and links
├── DVA-focused-Portfolio/    # React/Vite portfolio site (GitHub Pages)
├── DVA-oriented-Resume/      # Resume assets
├── requirements.txt
└── .gitignore
```

---

## Datasets

| File | Rows | Description |
|---|---|---|
| `transactions.csv` | 1,000,000 | One row per transaction — amounts, device, velocity, fraud label |
| `account_profiles.csv` | 50,000 | Per-account aggregates — risk score, fraud history, 2FA status |
| `fraud_patterns.csv` | 7 | Reference table of fraud types with aggregate stats |
| `network_edges.csv` | 7,411 | Account-to-account connections for fraud-ring detection |
| `time_series_stats.csv` | 26,280 | Hourly aggregated transaction and fraud metrics |

> `transactions.csv` is stored via **Git LFS** due to its size.

Full schema in [docs/data_dictionary.md](docs/data_dictionary.md).

---

## Pipeline

```
Raw CSVs → scripts/etl_pipeline.py → data/processed/
```

The ETL pipeline:
1. **Extracts** all five raw CSVs
2. **Transforms** — parses datetimes, handles nulls, casts booleans, engineers date and velocity features
3. **Loads** cleaned files to `data/processed/`

Run it with:

```bash
pip install -r requirements.txt
python -m scripts.etl_pipeline
```

---

## Notebooks

| Notebook | Purpose |
|---|---|
| `01_extraction` | Load raw data, inspect shapes and dtypes |
| `02_cleaning` | Handle missing values, fix types, remove duplicates |
| `03_eda` | Distribution plots, fraud rate by category/hour/country |
| `04_statistical_analysis` | Fraud pattern breakdown, risk scoring, network analysis |
| `05_final_load_prep` | Merge and export final dataset for Tableau and modelling |

---

## Key Findings

- **Card Not Present** is the most common fraud type (34.9 % of all fraud)
- Fraudulent transactions average **$730** vs **$174** for legitimate ones
- `crypto` and `money_transfer` merchant categories carry the highest fraud rates (5.3 % and 4.1 %)
- ~40 % of fraud occurs between midnight and 5 am
- Accounts without 2FA account for ~40 % of fraud cases

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data processing | Python, Pandas, NumPy |
| Analysis & visualisation | Matplotlib, Seaborn, Plotly, Jupyter |
| BI dashboard | Tableau |
| Portfolio site | React 19, Vite 8, GitHub Pages |
| Version control | Git, Git LFS |

---

## Setup

```bash
git clone https://github.com/AnanyaSoni2004/Global_Stock_Market_AnalysisDashboard
cd Global_Stock_Market_AnalysisDashboard
pip install -r requirements.txt
jupyter notebook
```

> Git LFS must be installed to pull `transactions.csv`:
> ```bash
> git lfs install
> git lfs pull
> ```
