from flask import Blueprint, jsonify, request
from firebase_admin import firestore

main = Blueprint('main', __name__)

# Initialize Firestore client (if not already imported/initialized elsewhere)
db = firestore.client()

@main.route('/')
def index():
    return jsonify({"message": "Welcome to the AI-Powered Gamified Financial Trust Score API!"})

@main.route('/trust_history')
def trust_history():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    # Reference to the user's trust_history subcollection.
    history_ref = db.collection("users").document(user_id).collection("trust_history")
    # Query all documents in the subcollection.
    docs = history_ref.stream()

    # Build a list of records.
    history_data = []
    for doc in docs:
        history_data.append(doc.to_dict())

    # Optionally sort the records by date.
    history_data.sort(key=lambda x: x["date"])

    return jsonify(history_data)
