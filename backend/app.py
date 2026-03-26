"""FastAPI app serving churn predictions."""

import os
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Churn Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = os.path.join(os.path.dirname(__file__), "model.joblib")
pipeline = joblib.load(model_path)


class PredictRequest(BaseModel):
    age: int
    gender: str
    tenure: int
    usage_frequency: int
    support_calls: int
    payment_delay: int
    subscription_type: str
    contract_length: str
    total_spend: float
    last_interaction: int


class PredictResponse(BaseModel):
    prediction: str
    probability: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    df = pd.DataFrame([{
        "Age": req.age,
        "Gender": req.gender,
        "Tenure": req.tenure,
        "Usage Frequency": req.usage_frequency,
        "Support Calls": req.support_calls,
        "Payment Delay": req.payment_delay,
        "Subscription Type": req.subscription_type,
        "Contract Length": req.contract_length,
        "Total Spend": req.total_spend,
        "Last Interaction": req.last_interaction,
    }])
    pred = pipeline.predict(df)[0]
    proba = pipeline.predict_proba(df)[0][1]
    return PredictResponse(
        prediction="churn" if pred == 1 else "no churn",
        probability=round(float(proba), 4),
    )
