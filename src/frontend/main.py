import streamlit as st
from auth import login_signup
from navbar import show_navbar

# Inject global CSS for a unified, vibrant look across the app
st.markdown(
    """
    <style>
        /* Global background gradient */
        .stApp {
            background: linear-gradient(135deg, #FDEB71, #F8D800);
        }
        /* Global header styling */
        .header {
            color: #2C3E50;
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px #BDC3C7;
        }
        /* Global subheader styling */
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
    """,
    unsafe_allow_html=True
)

def main():
    # Initialize session state for login if not already set
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Route the user: if logged in, show the navigation bar (and dashboard); otherwise, show login/signup.
    if not st.session_state["logged_in"]:
        login_signup()
    else:
        show_navbar()

if __name__ == "__main__":
    main()
