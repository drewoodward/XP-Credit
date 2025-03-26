import streamlit as st
from auth import login_signup
from navbar import show_navbar
import os

# Inject the background CSS at the top of the app.
main_background = """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #F8F4FF, #EFDECD);
    }
    </style>
    """
st.markdown(main_background, unsafe_allow_html=True)

def main():
    # Initialize session state for login if not already set.
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    st.logo("src/frontend/assets/X.png", size="large")
    logo_path = os.path.join(os.getcwd(), "src", "frontend","assets","X.png")
    print("Current file: ", os.path.join(os.getcwd(), "src", "frontend","assets","X.png"))

    # Route the user based on login status.
    if st.session_state["logged_in"]:
        show_navbar()  # Show the navigation bar and dashboard for logged-in users.
    else:
        login_signup()  # Show the login/signup form if not logged in.

if __name__ == "__main__":
    main()
