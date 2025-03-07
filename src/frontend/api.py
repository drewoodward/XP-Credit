import requests
import pandas as pd
import base64

API_URL = "http://127.0.0.1:5000"

def create_account(username):
    payload = {"username": username}
    response = requests.post(f"{API_URL}/create_account", json=payload)
    return response.json(), response.status_code

def update_trust_score(username, new_score):
    payload = {"username": username, "trust_score": new_score}
    response = requests.post(f"{API_URL}/update_trust_score", json=payload)
    return response.json(), response.status_code

def get_credit_score(user_id):
    response = requests.get(f"{API_URL}/credit_score?user_id={user_id}")
    if response.status_code == 200:
        return response.json().get("credit_score")
    return None

def get_trust_history(user_id):
    response = requests.get(f"{API_URL}/trust_history?user_id={user_id}")
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'], errors='coerce')
                df = df.sort_values(by='date')
            elif 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
                df = df.sort_values(by='timestamp')
            return df
    return None

def get_badges(user_id):
    try:
        response = requests.get(f"{API_URL}/badges?user_id={user_id}")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        # Log error if needed
        pass
    # Dummy badge list for testing
    return ["badges/badge1.png"]

def get_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
