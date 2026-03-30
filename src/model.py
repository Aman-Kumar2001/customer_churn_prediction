import pandas as pd
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from src.feature_creation import new_features
from src.preprocessing import preprocess_data
import joblib

train = pd.read_csv("data/train.csv", index_col='id')
print("Data set successfully loaded....")

y = train["Churn"]
X = train.drop(columns=["Churn"])

X, y = new_features(X, y)

print("New feature generated...")

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'AverageCharges', 'ServiceSupport', 'trusted', 'StreamService']

ord_cat_cols = ['Partner','Dependents', 'PhoneService','PaperlessBilling']

nom_cat_cols = ['gender', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection','TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']

preprocessing = preprocess_data(num_cols, ord_cat_cols, nom_cat_cols)

kf = KFold(n_splits=5, shuffle=True, random_state=1)
y = pd.DataFrame({"Churn":y})

print("Model training started....")

for fold, (tr_idx, val_idx) in enumerate(kf.split(X)):
    
    X_tr, X_val = X.iloc[tr_idx], X.iloc[val_idx]
    y_tr, y_val = y.iloc[tr_idx], y.iloc[val_idx]

    hgb_fold = HistGradientBoostingClassifier(
        learning_rate=0.05,
        max_iter = 1200,
        max_depth = 6,
        max_leaf_nodes=48,
        max_features= 0.5,
        l2_regularization=0.3,
        random_state=1,
        early_stopping=True,
        validation_fraction=0.1
    )

    model = Pipeline(steps=[("preprocessing", preprocessing),
                                    ("hgb_fold_model", hgb_fold)])
    
    model.fit(X_tr, y_tr)


print("Model finally trained, ready to be dumped....")
joblib.dump(model, "artifacts/model.pkl")

print("Model dumped successfully!")