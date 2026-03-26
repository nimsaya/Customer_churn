"""Train a logistic regression pipeline on the Kaggle customer churn dataset."""

import os
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

base = os.path.dirname(__file__)
train_df = pd.read_csv(os.path.join(base, "customer_churn_dataset-training-master.csv"))
test_df = pd.read_csv(os.path.join(base, "customer_churn_dataset-testing-master.csv"))

# Drop CustomerID and rows with missing values
train_df = train_df.drop(columns=["CustomerID"]).dropna()
test_df = test_df.drop(columns=["CustomerID"]).dropna()

feature_cols = [
    "Age", "Gender", "Tenure", "Usage Frequency", "Support Calls",
    "Payment Delay", "Subscription Type", "Contract Length",
    "Total Spend", "Last Interaction",
]

X_train = train_df[feature_cols]
y_train = train_df["Churn"]
X_test = test_df[feature_cols]
y_test = test_df["Churn"]

numeric_features = [
    "Age", "Tenure", "Usage Frequency", "Support Calls",
    "Payment Delay", "Total Spend", "Last Interaction",
]
categorical_features = ["Gender", "Subscription Type", "Contract Length"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000)),
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {acc:.3f}")

model_path = os.path.join(base, "model.joblib")
joblib.dump(pipeline, model_path)
print(f"Model saved to {model_path}")
