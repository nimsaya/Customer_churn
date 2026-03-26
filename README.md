# Customer Churn Predictor

A full-stack machine learning application that predicts whether a subscription service customer will churn (cancel their subscription). Built with a Python/FastAPI backend serving a trained scikit-learn model and a React frontend for interactive predictions.

## Motivation

Customer churn is one of the most important metrics for subscription-based businesses. Losing customers is expensive — acquiring a new customer costs significantly more than retaining an existing one. This project demonstrates how machine learning can be used to identify at-risk customers based on behavioral and account data, enabling businesses to take proactive retention actions before it's too late.

## Dataset

This project uses the [Customer Churn Dataset](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset) from Kaggle by Muhammad Shahid Azeem. It contains **440,000+** customer records with the following features:

| Feature | Description |
|---------|-------------|
| Age | Customer age |
| Gender | Male / Female |
| Tenure | Months as a customer |
| Usage Frequency | How often the customer uses the service |
| Support Calls | Number of support calls made |
| Payment Delay | Days of payment delay |
| Subscription Type | Basic, Standard, or Premium |
| Contract Length | Monthly, Quarterly, or Annual |
| Total Spend | Total amount spent ($) |
| Last Interaction | Days since last interaction |
| Churn | Whether the customer churned (target variable) |

The dataset comes pre-split into training and testing sets.

## Tech Stack

**Backend:**
- Python, FastAPI, scikit-learn, pandas, joblib

**Frontend:**
- React, Vite

**Model:**
- Logistic Regression with a scikit-learn Pipeline (StandardScaler + OneHotEncoder preprocessing)

## Project Structure

```
Customer_Churn/
├── backend/
│   ├── app.py                # FastAPI server with /health and /predict endpoints
│   ├── train_model.py        # Model training script
│   ├── generate_data.py      # Synthetic data generator (optional, not used)
│   ├── model.joblib           # Trained model pipeline
│   ├── requirements.txt       # Python dependencies
│   ├── customer_churn_dataset-training-master.csv
│   └── customer_churn_dataset-testing-master.csv
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # React form UI
│   │   └── App.css            # Styling
│   └── package.json
├── .env                       # Kaggle API credentials (not committed)
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+

### 1. Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Train the model

```bash
python train_model.py
```

This loads the dataset, trains a Logistic Regression pipeline, and saves it to `model.joblib`.

### 3. Start the backend

```bash
uvicorn app:app --reload
```

The API will be available at **http://localhost:8000**.

### 4. Install frontend dependencies and start

```bash
cd frontend
npm install
npm run dev
```

The UI will be available at **http://localhost:5173**.

## API Endpoints

**GET /health** — Health check
```json
{"status": "ok"}
```

**POST /predict** — Get a churn prediction
```json
{
  "age": 35,
  "gender": "Male",
  "tenure": 12,
  "usage_frequency": 10,
  "support_calls": 3,
  "payment_delay": 10,
  "subscription_type": "Standard",
  "contract_length": "Monthly",
  "total_spend": 500,
  "last_interaction": 15
}
```

Response:
```json
{
  "prediction": "churn",
  "probability": 0.7234
}
```

## Acknowledgments

- Dataset: [Customer Churn Dataset](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset) by Muhammad Shahid Azeem on Kaggle