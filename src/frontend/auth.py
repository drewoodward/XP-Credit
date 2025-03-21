import streamlit as st
from api import create_account, get_credit_score


def login_signup():
    if not st.session_state.logged_in:
        # Render the header in its own block without an overlay container.
        st.markdown(
            """
            <style>
            .header-container {
                text-align: center;
                padding: 1rem;
            }
            </style>
            <div class="header-container">
                <h1>XP-Credit</h1>
                <h2>A web app that evaluates financial trustworthiness through AI-driven insights while incentivizing responsible financial behaviors.</h2>
            </div>
            """, unsafe_allow_html=True
        )
        
        # Render the interactive login/signup form separately.
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
                    #commented out for debugging purposes
                    #st.experimental_rerun()  # Refresh UI after login

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
        # Display logged-in view.
        st.write(f"Welcome, {st.session_state.username}!")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_rerun()  # Refresh UI after logout

if __name__ == "__main__":
    login_signup()
