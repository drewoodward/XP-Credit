import requests
import pandas as pd
import base64
import streamlit as st

API_URL = "https://flask-api-529591304289.us-east4.run.app"

def create_account(username):
    payload = {"username": username}
    response = requests.post(f"{API_URL}/create_account", json=payload)

    #debugging the failed to decode json bs
    st.write("Response Status:", response.status_code)
    st.write("Response Text:", response.text)  # This will show if JSON is valid
    st.write("Response JSON:", response.json() if response.headers.get('Content-Type') == 'application/json' else "Invalid JSON")
    
    try:
        json_response = response.json()
    except ValueError:
        # Return a custom error message along with the raw response text for debugging.
        
        json_response = {"error": f"Failed to decode JSON: {response.text}"}
    return json_response, response.status_code

def update_trust_score(username, new_score):
    payload = {"username": username, "trust_score": new_score}
    response = requests.post(f"{API_URL}/update_trust_score", json=payload)
    try:
        json_response = response.json()
    except ValueError:
        json_response = {"error": f"Failed to decode JSON: {response.text}"}
    return json_response, response.status_code

def get_credit_score(user_id):
    response = requests.get(f"{API_URL}/credit_score?user_id={user_id}")
    if response.status_code == 200:
        try:
            return response.json().get("credit_score")
        except ValueError:
            return None
    return None

def get_trust_history(user_id):
    response = requests.get(f"{API_URL}/trust_history?user_id={user_id}")
    if response.status_code == 200:
        try:
            data = response.json()
        except ValueError:
            return None
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
            try:
                return response.json()  # Expecting a list of badge image URLs/paths
            except ValueError:
                return ["badges/badge1.png"]
    except Exception as e:
        # Log error if needed
        pass
    # Dummy badge list for testing
    return ["badges/badge1.png"]

def get_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
