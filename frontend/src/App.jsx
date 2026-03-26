import { useState } from "react";
import "./App.css";

const API_URL = "http://localhost:8000";

function App() {
  const [form, setForm] = useState({
    age: 35,
    gender: "Male",
    tenure: 12,
    usage_frequency: 10,
    support_calls: 3,
    payment_delay: 10,
    subscription_type: "Standard",
    contract_length: "Monthly",
    total_spend: 500,
    last_interaction: 15,
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: type === "number" ? Number(value) : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await fetch(`${API_URL}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error(`Server error: ${res.status}`);
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Customer Churn Predictor</h1>
      <p className="description">
        Predict whether a subscription service customer will cancel (churn).
        Built on a dataset of 440,000+ customers across Basic, Standard, and Premium
        plans with Monthly, Quarterly, and Annual contracts. Enter customer details
        below — the model analyzes tenure, usage, support calls, payment delays,
        and spending to estimate churn likelihood.
      </p>
      <form onSubmit={handleSubmit}>
        <label>
          Age
          <input type="number" name="age" value={form.age} onChange={handleChange} min="18" />
        </label>

        <label>
          Gender
          <select name="gender" value={form.gender} onChange={handleChange}>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </label>

        <label>
          Tenure (months)
          <input type="number" name="tenure" value={form.tenure} onChange={handleChange} min="0" />
        </label>

        <label>
          Usage Frequency
          <input type="number" name="usage_frequency" value={form.usage_frequency} onChange={handleChange} min="0" />
        </label>

        <label>
          Support Calls
          <input type="number" name="support_calls" value={form.support_calls} onChange={handleChange} min="0" />
        </label>

        <label>
          Payment Delay (days)
          <input type="number" name="payment_delay" value={form.payment_delay} onChange={handleChange} min="0" />
        </label>

        <label>
          Subscription Type
          <select name="subscription_type" value={form.subscription_type} onChange={handleChange}>
            <option value="Basic">Basic</option>
            <option value="Standard">Standard</option>
            <option value="Premium">Premium</option>
          </select>
        </label>

        <label>
          Contract Length
          <select name="contract_length" value={form.contract_length} onChange={handleChange}>
            <option value="Monthly">Monthly</option>
            <option value="Quarterly">Quarterly</option>
            <option value="Annual">Annual</option>
          </select>
        </label>

        <label>
          Total Spend ($)
          <input type="number" name="total_spend" value={form.total_spend} onChange={handleChange} min="0" step="0.01" />
        </label>

        <label>
          Last Interaction (days ago)
          <input type="number" name="last_interaction" value={form.last_interaction} onChange={handleChange} min="0" />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Predict"}
        </button>
      </form>

      {error && <div className="result error">{error}</div>}

      {result && (
        <div className={`result ${result.prediction === "churn" ? "churn" : "no-churn"}`}>
          <h2>{result.prediction === "churn" ? "Will Churn" : "Will Not Churn"}</h2>
          <p>Churn probability: {(result.probability * 100).toFixed(1)}%</p>
        </div>
      )}
    </div>
  );
}

export default App;
