# src/interpret/shap_analysis.py
import shap
import matplotlib.pyplot as plt
import os

def run_shap_analysis(model, X_train, X_test):
    """Run SHAP analysis on the trained model and save summary plot."""
    print("🔍 Running SHAP analysis...")
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)

    # Create directory if not exists
    os.makedirs("outputs/plots", exist_ok=True)

    # Save SHAP summary plot
    plt.figure()
    shap.summary_plot(shap_values, X_test, show=False)
    plt.savefig("outputs/plots/shap_summary_plot.png", bbox_inches="tight")
    plt.close()
    print("📊 SHAP summary plot saved to outputs/plots/shap_summary_plot.png")
