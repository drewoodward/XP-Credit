import torch
import pickle
import pandas as pd
import json
import requests
from datetime import datetime, timezone
from training_pytorch import X_test, y_test  # Import test data
from neural_network_pytorch import FinancialScoreModel  # Import model class

# Load the saved model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = FinancialScoreModel().to(device)

checkpoint = torch.load("financial_score_model.pth", map_location=device)
model.load_state_dict(checkpoint["model_state_dict"])
model.eval()

# Loss function for evaluation
criterion = torch.nn.MSELoss()

# Evaluate model on test data
X_test = X_test.to(device)
y_test = y_test.to(device)

with torch.no_grad():
    test_predictions = model(X_test)
    test_loss = criterion(test_predictions, y_test)

print(f"Test Loss: {test_loss.item():.4f}")

# Load scaler (assuming it was saved in training_pytorch.py)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Example new data (should match the number of features)
new_data = torch.tensor([[25, 55000, 200, 700, 0.25, 5000]], dtype=torch.float32)

# Convert new_data to a DataFrame with feature names
new_data_df = pd.DataFrame(new_data.numpy(), columns=["age", "income", "transaction_amount", "credit_score", "debt_to_income_ratio", "savings"])

# Normalize using the same scaler
new_data_scaled = scaler.transform(new_data_df)

# Convert back to a tensor and move to the correct device
new_data_tensor = torch.tensor(new_data_scaled, dtype=torch.float32).to(device)

# Make prediction
with torch.no_grad():
    predicted_score = model(new_data_tensor).item()

print(f"Predicted Financial Score: {predicted_score:.2f}")

# Create a JSON record with the predicted score, current timestamp, and username.
# Replace "testuser" with the appropriate user ID.
prediction_record = {
    "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "trust_score": predicted_score,
    "username": "testuser"
}

# Convert the record to a JSON string (for printing or debugging)
prediction_json = json.dumps(prediction_record, indent=4)
print("Prediction JSON:")
print(prediction_json)

# Send the JSON record to your Flask API's /update_trust_score endpoint.
response = requests.post("http://127.0.0.1:5000/update_trust_score", json=prediction_record)
if response.status_code in (200, 201):
    print("Prediction stored successfully!")
else:
    print("Error storing prediction:", response.text)
