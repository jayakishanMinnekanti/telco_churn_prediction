# src/model/train_default.py
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix

def train_default_model(X_train, y_train, X_test, y_test):
    model = XGBClassifier(eval_metric='logloss')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\n[Default Model]\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    return model