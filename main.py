# main.py
# Entry point to run the Telco Churn Prediction Pipeline

import os
from src.data.load_data import load_data
from src.data.preprocess import preprocess_data
from src.model import (
    train_default_model,
    train_tuned_model,
    train_weighted_model,
    train_smote_model
)
from src.interpret.shap_analysis import run_shap_analysis
from src.utils.save_model import save_model


def main():
    print("✅ Starting Telco Churn Pipeline...")

    # Load raw data
    data_path = "data/data.csv"
    df = load_data(data_path)

    # Preprocess and split
    X_train, X_test, y_train, y_test, df_clean = preprocess_data(df)

    # 1. Default model
    default_model = train_default_model(X_train, y_train, X_test, y_test)
    save_model(default_model, "outputs/models/default_model.pkl")

    # 2. Hyperparameter tuned model
    tuned_model = train_tuned_model(X_train, y_train, X_test, y_test)
    save_model(tuned_model, "outputs/models/tuned_model.pkl")

    # 3. Class-weighted model (used for SHAP)
    weighted_model = train_weighted_model(X_train, y_train, X_test, y_test)
    save_model(weighted_model, "outputs/models/weighted_model.pkl")

    # 4. SMOTE-balanced model
    smote_model = train_smote_model(X_train, y_train, X_test, y_test)
    save_model(smote_model, "outputs/models/smote_model.pkl")

    # 5. SHAP analysis (uses weighted model)

    run_shap_analysis(weighted_model, X_train, X_test)

    print("✅ Pipeline Completed Successfully.")


if __name__ == "__main__":
    os.makedirs("outputs/models", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)
    main()