import streamlit as st
from api import create_account, get_credit_score

# Ensure session state variables are initialized
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

def login_signup():
    if not st.session_state.logged_in:
        # Display login/signup form only if user is NOT logged in
        st.markdown("""
        <style>
        .centered-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 60vh; /* Adjust this value based on your layout needs */
            text-align: center;
        }
        </style>
        <div class="centered-container">
            <h1>XP-Credit</h1>
            <h2>A web app that evaluates financial trustworthiness through AI-driven insights while incentivizing responsible financial behaviors.</h2>
        </div>
        """, unsafe_allow_html=True)

        auth_mode = st.radio("***Choose an option***:", ["Login", "Sign Up"])
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")  

        if st.button("Submit"):
            if not username or not password:
                st.error("Please enter both username and password.")
                return

            if auth_mode == "Login":
                # Attempt to fetch the trust score to verify user existence.
                score = get_credit_score(username)
                if score is None:
                    st.error("Account not found. Please sign up first.")
                else:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Logged in successfully!")
                    st.experimental_rerun()  # Refresh UI after login

            elif auth_mode == "Sign Up":
                result, status = create_account(username)
                if status == 201:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Account created successfully! You are now logged in.")
                    st.experimental_rerun()  # Refresh UI after signup
                else:
                    st.error(result.get("error", "Sign up failed."))
    else:
        # this block of code is being executed for some reason or maybe its the showDashboard()
        st.write(f"Welcome, {st.session_state.username}!")

        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_rerun()  # Refresh UI after logout
