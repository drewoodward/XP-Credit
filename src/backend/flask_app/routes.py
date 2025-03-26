import logging
from flask import Blueprint, jsonify, request
from firebase_admin import firestore
from datetime import datetime, timezone

main = Blueprint('main', __name__)

# Initialize Firestore client (if not already imported/initialized elsewhere)
db = firestore.client()

@main.route('/')
def index():
    return jsonify({"message": "Welcome to the AI-Powered Gamified Financial Trust Score API!"})

@main.route('/create_account', methods=['POST'])
def create_account():
    """
    Expects JSON payload: {"username": "unique_username"}
    Creates a new user document with an initial trust score of (to be determined).
    """
    try:
        data = request.get_json()
        logging.debug(f"Received request data: {data}")

        if not data or "username" not in data:
            logging.warning("Invalid request: Missing username")
            return jsonify({"error": "Username is required"}), 400

        username = data["username"].strip()
        user_ref = db.collection("users").document(username)

        if user_ref.get().exists:
            logging.warning("Username already exists")
            return jsonify({"error": "Username already exists"}), 400

        user_ref.set({
            "username": username,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "trust_score": 0,
            "xp": 0
        })

        logging.info(f"Account created for username: {username}")
        return jsonify({"message": "Account created", "username": username}), 201

    except Exception as e:
        logging.error(f"Error in create_account: {str(e)}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500

@main.route('/update_trust_score', methods=['POST'])
def update_trust_score():
    """
    Expects JSON payload: {"username": "unique_username", "trust_score": new_score}
    Updates the user's trust score and appends a new record in the trust_history subcollection.
    """
    data = request.get_json()
    username = data.get("username")
    trust_score = data.get("trust_score")
    if not username or trust_score is None:
        return jsonify({"error": "Username and trust_score are required"}), 400

    user_ref = db.collection("users").document(username)
    if not user_ref.get().exists:
        return jsonify({"error": "User not found"}), 404

    # Update the current trust score
    user_ref.update({"trust_score": trust_score})
    
    # Add a new history record with a timestamp
    history_ref = user_ref.collection("trust_history")
    record_id = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    history_ref.document(record_id).set({
        "date": record_id,
        "trust_score": trust_score
    })

    return jsonify({"message": "Trust score updated"}), 200

@main.route('/get_xp')
def get_xp():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400
    
    user_ref = db.collection("users").document(user_id)
    user_snapshot = user_ref.get()
    if not user_snapshot.exists:
        return jsonify({"error": "User not found"}), 404
    
    user_data = user_snapshot.to_dict()
    xp = user_data.get("xp", 0)
    return jsonify({"xp": xp})

@main.route('/update_xp', methods=['POST'])
def update_xp():
    """
    Expects JSON payload: {"username": "unique_username", "xp_delta": xp_increase}
    Adds xp_delta to the user's existing XP.
    """
    data = request.get_json()
    username = data.get("username")
    xp_delta = data.get("xp_delta")
    if not username or xp_delta is None:
        return jsonify({"error": "Username and xp_delta are required"}), 400
    
    user_ref = db.collection("users").document(username)
    user_snapshot = user_ref.get()
    if not user_snapshot.exists:
        return jsonify({"error": "User not found"}), 404
    
    current_xp = user_snapshot.to_dict().get("xp", 0)
    new_xp = current_xp + xp_delta
    user_ref.update({"xp": new_xp})
    
    return jsonify({"message": "XP updated", "new_xp": new_xp}), 200

@main.route('/credit_score')
def credit_score():
    """
    Expects a query parameter: user_id.
    Returns the current trust score for the specified user.
    """
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    user_ref = db.collection("users").document(user_id)
    user_snapshot = user_ref.get()
    if not user_snapshot.exists:
        return jsonify({"error": "User not found"}), 404

    user_data = user_snapshot.to_dict()
    trust_score = user_data.get("trust_score", 0)
    return jsonify({"credit_score": trust_score})

@main.route('/trust_history')
def trust_history():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    # Reference to the user's trust_history subcollection.
    history_ref = db.collection("users").document(user_id).collection("trust_history")
    docs = history_ref.stream()

    history_data = []
    for doc in docs:
        history_data.append(doc.to_dict())

    # Optionally sort the records by date.
    history_data.sort(key=lambda x: x["date"])

    return jsonify(history_data)

@main.route('/badges')
def badges():
    """
    Dummy endpoint for badges.
    Expects a query parameter: user_id.
    Returns a JSON list of badge image paths.
    """
    print("I am in badges route")
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    # For demonstration purposes, return a static list.
    badge_list = ["src/frontend/badges/badge1.png", "src/frontend/badges/achievement-award.png"]
    return jsonify(badge_list)
