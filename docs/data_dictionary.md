# Data Dictionary — Global Stock Market Analysis: Fraud Detection

All raw data lives in `data/raw/`. Processed outputs are in `data/processed/`.

---

## Table of Contents

1. [transactions.csv](#1-transactionscsv)
2. [account_profiles.csv](#2-account_profilescsv)
3. [fraud_patterns.csv](#3-fraud_patternscsv)
4. [network_edges.csv](#4-network_edgescsv)
5. [time_series_stats.csv](#5-time_series_statscsv)
6. [Relationships](#relationships)

---

## 1. `transactions.csv`

**Rows:** 1,000,000 | **Columns:** 23 | **Storage:** Git LFS

One row per financial transaction. `is_fraud` is the target variable (1.71% positive rate).

| Column | Type | Description | Sample Values |
|---|---|---|---|
| `transaction_id` | string | Unique transaction identifier (primary key) | `TXN000000001` |
| `account_id` | string | Account that made the transaction (FK → `account_profiles`) | `ACC0016173` |
| `timestamp` | datetime | Date and time of transaction (ISO 8601) | `2023-02-21 08:02:38` |
| `hour_of_day` | int | Hour extracted from timestamp (0–23) | `8`, `23` |
| `day_of_week` | int | Day extracted from timestamp (0=Monday, 6=Sunday) | `1`, `5` |
| `is_weekend` | bool (0/1) | 1 if transaction occurred on Saturday or Sunday | `0`, `1` |
| `amount` | float | Transaction amount in USD | `168.42`, `85.78` |
| `merchant_category` | string | Merchant category label | `travel`, `crypto`, `grocery`, `gambling` |
| `mcc_code` | int | ISO Merchant Category Code | `4511`, `5999` |
| `merchant_country` | string | Two- or three-letter country code of merchant | `US`, `CA`, `AU` |
| `card_present` | bool (0/1) | 1 if physical card was present at point of sale | `0`, `1` |
| `device_type` | string | Device used for the transaction | `desktop`, `mobile`, `tablet` |
| `device_known` | bool (0/1) | 1 if device had been used by this account before | `0`, `1` |
| `ip_risk_score` | float | Risk score of originating IP address (0–100, higher = riskier) | `53.2`, `9.7` |
| `is_foreign_txn` | bool (0/1) | 1 if merchant country differs from account home country | `0`, `1` |
| `time_since_last_s` | int | Seconds elapsed since the account's previous transaction | `21`, `721` |
| `velocity_1h` | int | Number of transactions by this account in the prior hour | `0`, `2`, `5` |
| `amount_vs_avg_ratio` | float | Ratio of this transaction amount to the account's historical average | `2.64`, `0.73` |
| `account_age_days` | int | Age of the account in days at time of transaction | `3256`, `1527` |
| `has_2fa` | bool (0/1) | 1 if the account had 2-factor authentication enabled | `0`, `1` |
| `credit_limit` | float | Account credit limit in USD | `3958.46`, `11850.06` |
| `is_fraud` | bool (0/1) | **Target variable.** 1 if the transaction was fraudulent | `0`, `1` |
| `fraud_pattern` | string | Fraud type label; `No Fraud Pattern` for legitimate transactions | `card_not_present`, `account_takeover`, `No Fraud Pattern` |

**Key statistics:**

| Metric | Value |
|---|---|
| Total transactions | 1,000,000 |
| Fraudulent | 17,143 (1.71 %) |
| Avg amount — legitimate | $174.21 |
| Avg amount — fraudulent | $730.14 |
| Total fraud losses | $12.52 M |

**High-risk merchant categories (by fraud rate):** `crypto` (5.34 %), `money_transfer` (4.13 %)

---

## 2. `account_profiles.csv`

**Rows:** 50,000 | **Columns:** 23

One row per unique account. Contains behavioral aggregates computed from transaction history.

| Column | Type | Description | Sample Values |
|---|---|---|---|
| `account_id` | string | Unique account identifier (primary key) | `ACC0000001` |
| `account_age_days` | int | Account age in days | `353`, `2831` |
| `credit_limit` | float | Credit limit in USD | `2171.42`, `7533.75` |
| `home_country` | string | Account holder's home country | `US` |
| `risk_score` | float | Account-level risk score (0–100, higher = riskier) | `16.5`, `25.4` |
| `is_high_risk` | bool (0/1) | 1 if the account is flagged as high risk | `0`, `1` |
| `avg_txn_amount` | float | Mean transaction amount across account history (USD) | `90.82`, `63.78` |
| `avg_monthly_txns` | float | Mean number of transactions per month | `71.1`, `7.4` |
| `has_2fa` | bool (0/1) | 1 if 2-factor authentication is enabled | `0`, `1` |
| `account_type` | string | Account classification | `personal`, `business`, `premium` |
| `total_transactions` | float | Cumulative transaction count | `49.0`, `18.0` |
| `total_amount` | float | Cumulative transaction amount in USD | `7246.60`, `4435.69` |
| `avg_amount` | float | Mean transaction amount (USD) | `147.89`, `246.43` |
| `max_amount` | float | Largest single transaction in USD | `740.46`, `1175.86` |
| `fraud_count` | float | Number of confirmed fraudulent transactions | `0.0`, `1.0` |
| `fraud_amount` | float | Total USD value of confirmed fraudulent transactions | `0.0`, `186.13` |
| `pct_foreign` | float | Share of transactions that were international (0–1) | `0.35`, `0.17` |
| `avg_velocity` | float | Mean transactions per hour | `1.27`, `4.0` |
| `unique_countries` | float | Count of distinct merchant countries used | `9.0`, `3.0` |
| `unique_categories` | float | Count of distinct merchant categories used | `11.0`, `8.0` |
| `avg_ip_risk` | float | Mean IP risk score across all transactions (0–100) | `22.98`, `52.45` |
| `fraud_rate` | float | Fraud rate as a proportion (0–1) | `0.0`, `0.091` |
| `is_fraudster` | bool (0/1) | 1 if the account has been identified as a fraudster | `0.0`, `1.0` |

**Account type distribution:** `personal` 70.4 %, `business` 19.7 %, `premium` 9.9 %

---

## 3. `fraud_patterns.csv`

**Rows:** 7 | **Columns:** 12

Reference table. One row per fraud type with aggregate statistics.

| Column | Type | Description | Sample Values |
|---|---|---|---|
| `fraud_pattern` | string | Fraud type label (primary key) | `card_not_present`, `account_takeover` |
| `description` | string | Plain-language description of the fraud type | `"Online/CNP fraud — stolen card details used without physical card"` |
| `transaction_count` | int | Number of fraudulent transactions of this type | `5982`, `3432` |
| `fraud_share_pct` | float | Share of total fraud volume (%) | `34.89`, `20.02` |
| `avg_amount` | float | Mean transaction amount for this fraud type (USD) | `771.78`, `1203.13` |
| `median_amount` | float | Median transaction amount for this fraud type (USD) | `268.63`, `436.78` |
| `pct_night_0_5` | float | Share of transactions occurring midnight–5 am (%) | `~40–41` |
| `pct_foreign` | float | Share of transactions that are international (%) | `~55–60` |
| `pct_card_not_present` | float | Share of card-not-present transactions (%) | `~72–76` |
| `avg_velocity_1h` | float | Mean transactions per hour at time of fraud | `~3.93–4.04` |
| `avg_ip_risk` | float | Mean IP risk score at time of fraud | `~54–55` |
| `pct_no_2fa` | float | Share of accounts without 2FA at time of fraud (%) | `~39–44` |

**Fraud type breakdown:**

| Fraud Pattern | Count | Share |
|---|---|---|
| Card Not Present | 5,982 | 34.89 % |
| Account Takeover | 3,432 | 20.02 % |
| Card Present Stolen | 3,120 | 18.20 % |
| Friendly Fraud | 1,726 | 10.07 % |
| ATM Fraud | 1,216 | 7.09 % |
| Money Laundering | 1,011 | 5.90 % |
| Identity Theft | 656 | 3.83 % |

---

## 4. `network_edges.csv`

**Rows:** 7,411 | **Columns:** 6

One row per pairwise connection between two accounts sharing a common identifier (device, IP, phone, email domain). Used for fraud-ring detection.

| Column | Type | Description | Sample Values |
|---|---|---|---|
| `account_a` | string | First account in the connection (FK → `account_profiles`) | `ACC0017803` |
| `account_b` | string | Second account in the connection (FK → `account_profiles`) | `ACC0040032` |
| `shared_type` | string | The type of shared identifier | `phone`, `email_domain`, `ip_address`, `device_id` |
| `connection_count` | int | Number of times this pair shares the identifier | `7`, `13` |
| `ring_id` | string | Fraud ring identifier; `Unknown` if not part of a known ring | `RING0001`, `RING0002`, `Unknown` |
| `both_fraud` | bool (0/1) | 1 if both accounts are confirmed fraudsters | `0`, `1` |

**Notes:**
- 3,000 of 7,411 edges have `ring_id = Unknown` (originally null, filled during cleaning).
- The graph is undirected — each edge appears once with `account_a` / `account_b` assigned arbitrarily.

---

## 5. `time_series_stats.csv`

**Rows:** 26,280 | **Columns:** 10

Pre-aggregated hourly statistics. One row per hour covering approximately 3 years (2022–2024).

| Column | Type | Description | Sample Values |
|---|---|---|---|
| `hour` | datetime | Hour timestamp (YYYY-MM-DD HH:00:00, primary key) | `2022-01-01 00:00:00` |
| `transaction_count` | int | Total transactions in this hour | `40`, `47` |
| `fraud_count` | int | Fraudulent transactions in this hour | `0`, `2` |
| `total_amount` | float | Sum of all transaction amounts in this hour (USD) | `9341.66`, `10763.95` |
| `avg_amount` | float | Mean transaction amount in this hour (USD) | `233.54`, `262.54` |
| `avg_ip_risk` | float | Mean IP risk score across all transactions in this hour | `19.92`, `25.87` |
| `fraud_rate` | float | Fraction of transactions that were fraudulent (0–1) | `0.0`, `0.051` |
| `hour_of_day` | int | Hour of day extracted from `hour` (0–23) | `0`, `7` |
| `day_of_week` | int | Day of week extracted from `hour` (0=Monday, 6=Sunday) | `5` |
| `is_weekend` | bool (0/1) | 1 if the hour falls on Saturday or Sunday | `0`, `1` |

---

## Relationships

```
account_profiles (account_id) ──< transactions (account_id)
account_profiles (account_id) ──< network_edges (account_a)
account_profiles (account_id) ──< network_edges (account_b)
transactions (fraud_pattern)  >── fraud_patterns (fraud_pattern)
time_series_stats              — standalone (aggregated from transactions)
```

### Entity counts

| Dataset | Rows | Primary Key |
|---|---|---|
| `transactions` | 1,000,000 | `transaction_id` |
| `account_profiles` | 50,000 | `account_id` |
| `fraud_patterns` | 7 | `fraud_pattern` |
| `network_edges` | 7,411 | (`account_a`, `account_b`) |
| `time_series_stats` | 26,280 | `hour` |
