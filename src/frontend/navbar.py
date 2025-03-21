import streamlit as st
from streamlit_navigation_bar import st_navbar
from dashboard import show_dashboard
from auth import login_signup

def show_navbar():
    # Only one page: Dashboard.
    pages = ["Dashboard", "Login/Signup"]
    
    # Define your custom styles.
    styles = {
        "nav": {
            "background-color": "#eeddf3",
            "width": "100%",
            "margin": "0",
            "padding": "0"
        },
        "div": {
            "max-width": "32rem",
        },
        "span": {
            "border-radius": "0.5rem",
            "color": "#31333F",
            "margin": "0 0.125rem",
            "padding": "0.4375rem 0.625rem",
        },
        "active": {
            "background-color": "rgba(255, 255, 255, 0.25)",
        },
        "hover": {
            "background-color": "rgba(255, 255, 255, 0.35)",
        },
    }

    # Ensure a default page is set.
    if 'page' not in st.session_state:
        st.session_state.page = "Login/Signup"

    # Render the navbar.
    page = st_navbar(pages, styles=styles)
    st.session_state.page = page

    # Only one option: Dashboard.
    # for some reason this was showing the dashboard while in the login screen
    if st.session_state.page == "Dashboard":
        show_dashboard()

    if st.session_state.page == "Login/Signup":
        login_signup()
