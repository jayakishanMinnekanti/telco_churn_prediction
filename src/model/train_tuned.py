# src/model/train_tuned.py
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

def train_tuned_model(X_train, y_train, X_test, y_test):
    param_grid = {
        'max_depth': [3, 5, 7],
        'n_estimators': [100, 200],
        'learning_rate': [0.01, 0.1, 0.2]
    }
    grid = GridSearchCV(
        estimator=XGBClassifier(eval_metric='logloss'),
        param_grid=param_grid,
        scoring='f1',
        cv=3,
        verbose=1,
        n_jobs=-1
    )
    grid.fit(X_train, y_train)
    print("Best Parameters:", grid.best_params_)

    best_model = grid.best_estimator_
    y_pred = best_model.predict(X_test)
    print("\n[Tuned Model]\nClassification Report:\n", classification_report(y_test, y_pred))
    return best_model