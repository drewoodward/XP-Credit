#sets up firestore and helper functions for data management
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Use an environment variable to reference your service account key securely
SERVICE_ACCOUNT_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "/root/gamified_credit/gamified-credit/src/backend/flask_app/gamified-credit-firebase-adminsdk-fbsvc-497ccea0c6.json")

# Initialize the Firebase app if it hasn't been initialized already.
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()
