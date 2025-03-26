import pandas as pd
import numpy as np
import torch
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv(r"C:\Users\rrjar\OneDrive\Desktop\MIS4153\FinAI_2.0\V2_synthetic_financial_data.csv")

# Aggregate transactions per user
user_features = df.groupby("user_id").agg(
    age=("age", "first"),
    income=("income", "first"),
    credit_score=("credit_score", "first"),
    debt_to_income_ratio=("debt_to_income_ratio", "first"),
    savings=("savings", "first"),
    total_spent=("transaction_amount", "sum"),
    avg_transaction_amount=("transaction_amount", "mean"),
    spending_std=("transaction_amount", "std"),
    num_transactions=("transaction_amount", "count"),
    on_time_payment_ratio=("payment_made_on_time", "mean")
).reset_index()

# Fill NaN values (e.g., standard deviation of a single transaction)
user_features["spending_std"].fillna(0, inplace=True)

# Define features and target
features = [
    "age", "income", "credit_score", "debt_to_income_ratio", "savings", 
    "total_spent", "avg_transaction_amount", "spending_std", "num_transactions", 
    "on_time_payment_ratio"
]
X = user_features[features]

# Define the new target variable
y = (user_features["on_time_payment_ratio"] * 100) + (user_features["savings"] / 500) - (user_features["debt_to_income_ratio"] * 100)

# Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save the scaler
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Convert to tensors
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X_tensor, y_tensor, test_size=0.2, random_state=42)

print("Data successfully preprocessed and aggregated per user!")
