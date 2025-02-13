import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Generate 1,000 synthetic users
num_users = 1000
data = []

for _ in range(num_users):
    user_id = fake.uuid4()
    age = random.randint(18, 70)
    income = round(random.uniform(20000, 150000), 2)
    transaction_type = random.choice(["Rent", "Groceries", "Shopping", "Utilities", "Dining", "Travel"])
    transaction_amount = round(random.uniform(10, 5000), 2)
    due_date = fake.date_between(start_date="-1y", end_date="today")
    payment_made_on_time = random.choice([True, False])
    credit_score = round(random.uniform(300, 850), 2)  # FICO Score Range
    debt_to_income_ratio = round(random.uniform(0.1, 0.6), 2)
    savings = round(random.uniform(100, 50000), 2)
    
    # Example scoring formula (adjust for real ML model)
    financial_score = credit_score * (0.5 if not payment_made_on_time else 1) - (debt_to_income_ratio * 100)

    data.append([user_id, age, income, transaction_type, transaction_amount, due_date, payment_made_on_time, credit_score, debt_to_income_ratio, savings, financial_score])

df = pd.DataFrame(data, columns=[
    "user_id", "age", "income", "transaction_type", "transaction_amount",
    "due_date", "payment_made_on_time", "credit_score", "debt_to_income_ratio", "savings", "financial_score"
])

df.to_csv("synthetic_financial_data.csv", index=False)
print("Synthetic data saved to CSV!")
