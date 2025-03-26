# firestore_listener.py
import threading
import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key file
SERVICE_ACCOUNT_PATH = "./gamified-credit-firebase-adminsdk-fbsvc-497ccea0c6.json"

# Initialize the Firebase app (if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Global cache for the trust score (for example purposes)
trust_score_cache = {"trust_score": 0}

def on_snapshot(doc_snapshot, changes, read_time):
    """Callback function that updates the trust_score_cache when Firestore data changes."""
    for doc in doc_snapshot:
        data = doc.to_dict()
        # Update the global cache with the new trust score value.
        trust_score_cache["trust_score"] = data.get("trust_score", 0)
        print(f"[Firestore Listener] Trust Score updated: {trust_score_cache['trust_score']}")

def start_firestore_listener():
    """Starts a listener on a specific document in Firestore."""
    # Replace 'user_id' with the actual document ID you want to track.
    doc_ref = db.collection("users").document("user_id")
    # Set up the snapshot listener
    doc_ref.on_snapshot(on_snapshot)

def start_listener_in_background():
    """Starts the Firestore listener in a daemon thread."""
    listener_thread = threading.Thread(target=start_firestore_listener, daemon=True)
    listener_thread.start()