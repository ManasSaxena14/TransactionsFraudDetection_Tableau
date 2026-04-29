def add_transaction_date_features(transactions_df):
    """
    Create date features from transaction timestamp.
    """

    transactions_df["transaction_year"] = (
        transactions_df["timestamp"].dt.year
    )

    transactions_df["transaction_month"] = (
        transactions_df["timestamp"].dt.month
    )

    transactions_df["transaction_month_name"] = (
        transactions_df["timestamp"].dt.month_name()
    )

    transactions_df["transaction_day_name"] = (
        transactions_df["timestamp"].dt.day_name()
    )

    return transactions_df


def add_stats_date_features(time_series_stats_df):
    """
    Create date features from hour column.
    """

    time_series_stats_df["stats_year"] = (
        time_series_stats_df["hour"].dt.year
    )

    time_series_stats_df["stats_month"] = (
        time_series_stats_df["hour"].dt.month
    )

    time_series_stats_df["stats_month_name"] = (
        time_series_stats_df["hour"].dt.month_name()
    )

    time_series_stats_df["stats_day_name"] = (
        time_series_stats_df["hour"].dt.day_name()
    )

    return time_series_stats_df