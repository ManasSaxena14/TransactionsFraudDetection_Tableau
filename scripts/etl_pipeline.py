from scripts.utils import (
    load_csv,
    save_csv,
    print_shape
)

from scripts.preprocess import (
    convert_datetime_columns,
    handle_missing_values,
    convert_boolean_columns
)

from scripts.feature_engineering import (
    add_transaction_date_features,
    add_stats_date_features
)


def run_etl_pipeline():
    """
    Main ETL pipeline:
    Extract -> Transform -> Load
    """

    # -------------------------
    # Extract
    # -------------------------
    account_profiles_df = load_csv(
        "account_profiles.csv"
    )

    fraud_patterns_df = load_csv(
        "fraud_patterns.csv"
    )

    network_edges_df = load_csv(
        "network_edges.csv"
    )

    time_series_stats_df = load_csv(
        "time_series_stats.csv"
    )

    transactions_df = load_csv(
        "transactions.csv"
    )

    # -------------------------
    # Transform
    # -------------------------

    # Datetime conversion
    time_series_stats_df, transactions_df = (
        convert_datetime_columns(
            time_series_stats_df,
            transactions_df
        )
    )

    # Missing values
    network_edges_df, transactions_df = (
        handle_missing_values(
            network_edges_df,
            transactions_df
        )
    )

    # Feature engineering
    transactions_df = (
        add_transaction_date_features(
            transactions_df
        )
    )

    time_series_stats_df = (
        add_stats_date_features(
            time_series_stats_df
        )
    )

    # Boolean conversion
    (
        account_profiles_df,
        network_edges_df,
        time_series_stats_df,
        transactions_df
    ) = convert_boolean_columns(
        account_profiles_df,
        network_edges_df,
        time_series_stats_df,
        transactions_df
    )

    # -------------------------
    # Load
    # -------------------------
    save_csv(
        account_profiles_df,
        "account_profiles_clean.csv"
    )

    save_csv(
        fraud_patterns_df,
        "fraud_patterns_clean.csv"
    )

    save_csv(
        network_edges_df,
        "network_edges_clean.csv"
    )

    save_csv(
        time_series_stats_df,
        "time_series_stats_clean.csv"
    )

    save_csv(
        transactions_df,
        "transactions_clean.csv"
    )

    # -------------------------
    # Logs
    # -------------------------
    print_shape(
        "Account Profiles",
        account_profiles_df
    )

    print_shape(
        "Fraud Patterns",
        fraud_patterns_df
    )

    print_shape(
        "Network Edges",
        network_edges_df
    )

    print_shape(
        "Time Series Stats",
        time_series_stats_df
    )

    print_shape(
        "Transactions",
        transactions_df
    )

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_etl_pipeline()