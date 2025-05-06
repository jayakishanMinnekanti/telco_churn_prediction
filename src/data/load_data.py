# src/data/load_data.py
import pandas as pd

def load_data(path):
    """Load the Telco Churn dataset."""
    return pd.read_csv(path)