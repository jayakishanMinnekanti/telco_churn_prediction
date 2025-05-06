# src/model/train_smote.py
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import numpy as np

def train_smote_model(X_train, y_train, X_test, y_test):
    smote = SMOTE(random_state=42)
    X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)
    print("Original y_train:", np.bincount(y_train))
    print("After SMOTE:", np.bincount(y_train_sm))
    model = XGBClassifier(eval_metric='logloss')
    model.fit(X_train_sm, y_train_sm)
    y_pred = model.predict(X_test)
    print("\n[SMOTE Model]\nClassification Report:\n", classification_report(y_test, y_pred))
    return model