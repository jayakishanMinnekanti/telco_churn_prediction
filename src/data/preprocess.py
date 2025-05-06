# src/data/preprocess.py
import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split

def preprocess_data(df):
    # Drop unnecessary column
    df.drop('customerID', axis=1, inplace=True)

    # Convert 'TotalCharges' to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(subset=['TotalCharges'], inplace=True)

    # Encode target variable
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Save dropped categories for reproducibility
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    dropped_categories = {col: df[col].sort_values().unique()[0] for col in cat_cols}
    with open("outputs/dropped_categories.json", "w") as f:
        json.dump(dropped_categories, f)

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    # 💡 Force all columns to float (SHAP requires numeric input)
    df = df.astype(float)

    # Train/test split
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test, df