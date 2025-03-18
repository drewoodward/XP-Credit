import streamlit as st
from api import create_account, get_credit_score

# Application Title Page

def login_signup():
    st.markdown("<div class='header'>Welcome to Gamified Credit</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Login or Sign Up</div>", unsafe_allow_html=True)
    
    auth_mode = st.radio("Choose an option:", ("Login", "Sign Up"))
    username = st.text_input("Enter your unique username:")
    password = st.text_input("Enter your password:", type="password")  # Dummy password for demonstration,,, double check this
                                                                       # Also in real application we would implement proper pw handling
    
    if st.button("Submit"):
        if not username or not password:
            st.error("Please enter both username and password.")
            return
        if auth_mode == "Login":
            # For demo, we attempt to fetch the trust score to verify user existence.
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
