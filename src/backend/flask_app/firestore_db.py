# sets up firestore and helper functions for data management
import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
import json

# Load Firebase credentials from Streamlit Secrets
firebase_credentials = json.loads(st.secrets["FIREBASE_CREDENTIALS"])

# Initialize Firebase App if it hasn't been initialized already
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials)
    firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()
