import pandas as pd


def convert_datetime_columns(time_series_stats_df, transactions_df):
    """
    Convert datetime columns.
    """
    time_series_stats_df["hour"] = pd.to_datetime(
        time_series_stats_df["hour"]
    )

    transactions_df["timestamp"] = pd.to_datetime(
        transactions_df["timestamp"]
    )

    return time_series_stats_df, transactions_df


def handle_missing_values(network_edges_df, transactions_df):
    """
    Fill missing values.
    """
    network_edges_df["ring_id"] = network_edges_df["ring_id"].fillna(
        "Unknown"
    )

    transactions_df["fraud_pattern"] = (
        transactions_df["fraud_pattern"].fillna(
            "No Fraud Pattern"
        )
    )

    return network_edges_df, transactions_df


def convert_boolean_columns(
    account_profiles_df,
    network_edges_df,
    time_series_stats_df,
    transactions_df
):
    """
    Convert binary columns to boolean.
    """

    account_cols = [
        "is_high_risk",
        "has_2fa",
        "is_fraudster"
    ]

    txn_cols = [
        "card_present",
        "device_known",
        "is_foreign_txn",
        "has_2fa",
        "is_fraud"
    ]

    for col in account_cols:
        account_profiles_df[col] = (
            account_profiles_df[col].astype(bool)
        )

    network_edges_df["both_fraud"] = (
        network_edges_df["both_fraud"].astype(bool)
    )

    for col in txn_cols:
        transactions_df[col] = (
            transactions_df[col].astype(bool)
        )

    time_series_stats_df["is_weekend"] = (
        time_series_stats_df["is_weekend"].astype(bool)
    )

    return (
        account_profiles_df,
        network_edges_df,
        time_series_stats_df,
        transactions_df
    )