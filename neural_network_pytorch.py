from training_pytorch import X_train, y_train, features, X_test, y_test
import torch
import torch.nn as nn
import torch.optim as optim

# Random seed for reproducibility
torch.manual_seed(42)

# Define a simple neural network
class FinancialScoreModel(nn.Module):
    def __init__(self):
        super(FinancialScoreModel, self).__init__()
        self.fc1 = nn.Linear(len(features), 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# Initialize model, loss function, and optimizer
model = FinancialScoreModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
epochs = 500
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    predictions = model(X_train)
    loss = criterion(predictions, y_train)
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

print("Training complete!")


# Evaluate model on test data
model.eval()  # Set model to evaluation mode
with torch.no_grad():  # Disable gradient calculations for efficiency
    test_predictions = model(X_test)
    test_loss = criterion(test_predictions, y_test)

print(f"Test Loss: {test_loss.item():.4f}")

# Save model and optimizer
torch.save({
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': test_loss.item(),
}, "financial_score_model.pth")

print("Model and optimizer saved successfully!")