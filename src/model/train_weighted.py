# src/model/train_weighted.py
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import numpy as np

def train_weighted_model(X_train, y_train, X_test, y_test):
    scale_pos_weight = len(y_train[y_train == 0]) / len(y_train[y_train == 1])
    print("Scale Pos Weight:", scale_pos_weight)
    model = XGBClassifier(eval_metric='logloss', scale_pos_weight=scale_pos_weight)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\n[Weighted Model]\nClassification Report:\n", classification_report(y_test, y_pred))
    return model