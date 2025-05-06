# src/utils/save_model.py
import joblib

def save_model(model, path):
    joblib.dump(model, path)
    print(f"Model saved to: {path}")
