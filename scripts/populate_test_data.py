import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta

# Update the path below to your service account key JSON file.
SERVICE_ACCOUNT_PATH = "/root/gamified_credit/gamified-credit/src/backend/flask_app/gamified-credit-firebase-adminsdk-fbsvc-497ccea0c6.json"

# Initialize Firebase Admin SDK if not already initialized.
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Define a test user ID.
user_id = "testuser"

# Reference to the test user's document in the "users" collection.
user_ref = db.collection("users").document(user_id)

# Create a subcollection "trust_history" for historical records.
history_collection = user_ref.collection("trust_history")

# Populate test data: one record per day for the past 365 days.
for i in range(365):
    # Calculate the date for this record.
    record_date = datetime.now() - timedelta(days=i)
    # Format the date as a string (e.g., "2023-03-01") to use as the document ID.
    doc_id = record_date.strftime("%Y-%m-%d")
    # Create a dummy trust score (for example, starting at 600 and increasing each day).
    trust_score = 600 + i
    # Write the document in the "trust_history" subcollection.
    history_collection.document(doc_id).set({
        "date": doc_id,
        "trust_score": trust_score
    })

print("Test data successfully populated for user 'testuser'.")
