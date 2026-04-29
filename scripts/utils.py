import pandas as pd
from pathlib import Path

# Folder paths
RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")


def ensure_processed_folder():
    """
    Create processed folder if it does not exist.
    """
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)


def load_csv(filename):
    """
    Load CSV file from data/raw folder.
    """
    return pd.read_csv(RAW_PATH / filename)


def save_csv(df, filename):
    """
    Save DataFrame to data/processed folder.
    """
    ensure_processed_folder()
    df.to_csv(PROCESSED_PATH / filename, index=False)


def print_shape(name, df):
    """
    Print dataset shape.
    """
    print(f"{name}: {df.shape}")