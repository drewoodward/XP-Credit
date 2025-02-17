import streamlit as st
import pandas as pd
import requests
import random
import base64

# Define your Flask API base URL
API_URL = "http://127.0.0.1:5000"

# Inject custom CSS for a colorful, vibrant look
st.markdown("""
    <style>
        /* Overall background */
        .reportview-container {
            background: linear-gradient(135deg, #FDEB71, #F8D800);
        }
        /* Header styling */
        .header {
            color: #2C3E50;
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px #BDC3C7;
        }
        /* Subheader styling */
        .subheader {
            color: #2980B9;
            font-size: 1.75em;
            margin-bottom: 10px;
        }
        /* Button styling */
        .stButton>button {
            background-color: #1ABC9C;
            color: white;
            font-size: 1.2em;
            border-radius: 8px;
            padding: 10px 24px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #16A085;
        }
        /* Input styling */
        .stTextInput>div>input {
            background-color: #ECF0F1;
            color: #2C3E50;
            font-size: 1.1em;
            border-radius: 5px;
            padding: 8px;
        }
        /* Success & error messages */
        .error { color: #E74C3C; font-weight: bold; }
        .success { color: #27AE60; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ---------------- Backend API Functions ----------------

def create_account(username):
    payload = {"username": username}
    response = requests.post(f"{API_URL}/create_account", json=payload)
    return response.json(), response.status_code

def update_trust_score(username, new_score):
    payload = {"username": username, "trust_score": new_score}
    response = requests.post(f"{API_URL}/update_trust_score", json=payload)
    return response.json(), response.status_code

def get_credit_score(user_id):
    """
    Call the Flask API to get the current trust score for a given user.
    """
    response = requests.get(f"{API_URL}/credit_score?user_id={user_id}")
    if response.status_code == 200:
        return response.json().get("credit_score")
    else:
        return None

def get_trust_history(user_id):
    """
    Call the Flask API to get historical trust score data for the past year.
    Expects a JSON response with a list of records containing 'date' (or 'timestamp') and 'trust_score'.
    """
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
    """
    Call the Flask API to get the badges earned by the user.
    Expects a JSON response, for example: ["badges/badge1.png", "badges/badge2.png"]
    If the endpoint is unavailable, returns a dummy list for demonstration.
    """
    try:
        response = requests.get(f"{API_URL}/badges?user_id={user_id}")
        if response.status_code == 200:
            return response.json()  # Expecting a list of badge image URLs/paths
    except Exception as e:
        st.error(f"Error fetching badges: {e}")
    # Dummy badges for testing
    return ["badges/badge1.png"]

# ---------------- User Login / Sign Up ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

def login_signup():
    st.markdown("<div class='header'>Welcome to Gamified Credit</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Login or Sign Up</div>", unsafe_allow_html=True)
    
    # Let the user choose between logging in and signing up
    auth_mode = st.radio("Choose an option:", ("Login", "Sign Up"))
    username = st.text_input("Enter your unique username:")
    password = st.text_input("Enter your password:", type="password")  # Dummy password for now
    
    if st.button("Submit"):
        if not username or not password:
            st.error("Please enter both username and password.")
            return
        if auth_mode == "Login":
            # For demonstration, we'll attempt to retrieve the trust score to check if user exists.
            score = get_credit_score(username)
            if score is None:
                st.error("Account not found. Please sign up first.")
            else:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Logged in successfully!")
        elif auth_mode == "Sign Up":
            result, status = create_account(username)
            if status == 201:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Account created successfully! You are now logged in.")
            else:
                st.error(result.get("error", "Sign up failed."))

# ---------------- Main Dashboard ----------------

def dashboard():
    st.markdown(f"<div class='header'>Welcome, {st.session_state.username}!</div>", unsafe_allow_html=True)
    
    # Display current trust score
    score = get_credit_score(st.session_state.username)
    if score is not None:
        st.metric("Current Trust Score", score)
    else:
        st.write("Error fetching trust score.")
    
    # Simulated bank linking section
    st.markdown("<div class='subheader'>Link Your Bank Account</div>", unsafe_allow_html=True)
    st.write("Click the button below to log into your bank via Plaid (simulation).")
    if st.button("Link Bank Account"):
        st.success("Bank account linked successfully!")
        # Simulate AI model: compute new trust score (dummy value)
        new_trust_score = random.randint(600, 800)
        update_result, update_status = update_trust_score(st.session_state.username, new_trust_score)
        if update_status == 200:
            st.success("Trust score updated!")
        else:
            st.error("Failed to update trust score.")
    
    # Display historical trust score data and graph
    st.markdown("<div class='subheader'>Trust Score History (Past Year)</div>", unsafe_allow_html=True)
    df_history = get_trust_history(st.session_state.username)
    if df_history is not None and not df_history.empty:
        st.write("Historical Data Preview:")
        st.write(df_history.head())
        if 'date' in df_history.columns:
            st.line_chart(df_history.set_index('date')['trust_score'])
        elif 'timestamp' in df_history.columns:
            st.line_chart(df_history.set_index('timestamp')['trust_score'])
    else:
        st.write("No historical trust score data available.")
    
    # Convert the achievement image to a Base64 string
    achievement_image_path = "badges/achievement-award.png"
    try:
        encoded_image = get_image_as_base64(achievement_image_path)
    except Exception as e:
        st.error(f"Error loading achievement image: {e}")
        encoded_image = ""
    
    # Build the HTML for the header with the image embedded as Base64
    image_html = f'<img src="data:image/png;base64,{encoded_image}" style="height: 50px; margin-left: 10px;">'
    st.markdown(f"""
        <div class='subheader' style='display: flex; align-items: center; justify-content: center;'>
            Your Badges {image_html}
        </div>
    """, unsafe_allow_html=True)
    
    # Display badges for Saving Streak
    badges = get_badges(st.session_state.username)
    if badges:
        cols = st.columns(len(badges))
        for idx, col in enumerate(cols):
            with col:
                st.image(badges[idx], width=100)
                st.markdown("<div style='color:#2980B9; font-size: 1em; font-weight: bold;'>Saving Streak, +5 Trust Score Points!</div>", unsafe_allow_html=True)
    else:
        st.write("No badges earned yet.")
    
    # Display badges for Course Completed
    if badges:
        cols = st.columns(len(badges))
        for idx, col in enumerate(cols):
            with col:
                st.image(badges[idx], width=100)
                st.markdown("<div style='color:#2980B9; font-size: 1em; font-weight: bold;'>Course Completed, +5 Trust Score Points!</div>", unsafe_allow_html=True)
    else:
        st.write("No course completion badges earned yet.")

#helper function to print images
def get_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string
# ---------------- Main Application ----------------

def main():
    if not st.session_state.logged_in:
        login_signup()
    else:
        dashboard()

if __name__ == "__main__":
    main()
