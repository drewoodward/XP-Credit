import torch
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data/synthetic_financial_data.csv")

# Select features and target
features = ["age", "income", "transaction_amount", "credit_score", "debt_to_income_ratio", "savings"]
X = df[features]
y = df["financial_score"]

# Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save the scaler for later use in predictions
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Convert to tensors
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X_tensor, y_tensor, test_size=0.2, random_state=42)

if __name__ == "__main__":
    print("Data prepared for PyTorch model!")