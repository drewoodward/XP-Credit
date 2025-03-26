import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Parameters
num_users = 1000  
min_transactions = 5  
max_transactions = 50  

data = []

for _ in range(num_users):
    user_id = fake.uuid4()
    age = random.randint(18, 70)
    income = round(random.uniform(20000, 150000), 2)
    credit_score = round(random.uniform(300, 850), 2)
    debt_to_income_ratio = round(random.uniform(0.1, 0.6), 2)
    savings = round(random.uniform(100, 50000), 2)
    
    # Generate random number of transactions per user
    num_transactions = random.randint(min_transactions, max_transactions)
    
    for _ in range(num_transactions):
        transaction_type = random.choice(["Rent", "Groceries", "Shopping", "Utilities", "Dining", "Travel"])
        transaction_amount = round(random.uniform(10, 5000), 2)
        due_date = fake.date_between(start_date="-1y", end_date="today")
        payment_made_on_time = random.choice([True, False])
        
        data.append([
            user_id, age, income, transaction_type, transaction_amount, due_date,
            payment_made_on_time, credit_score, debt_to_income_ratio, savings
        ])

# Convert to DataFrame
df = pd.DataFrame(data, columns=[
    "user_id", "age", "income", "transaction_type", "transaction_amount", "due_date",
    "payment_made_on_time", "credit_score", "debt_to_income_ratio", "savings"
])

df.to_csv("FinAI_2.0/V2_synthetic_financial_data.csv", index=False)
print("Synthetic data with multiple transactions per user saved to CSV!")
