import streamlit as st
from streamlit_navigation_bar import st_navbar
from dashboard import show_dashboard
from auth import login_signup

# Additional pages (e.g., stock_dashboard, portfolio_simulator) can be imported here if needed.

def show_navbar():
    # Example: A sidebar navigation using a radio button for page selection.
    page = st.sidebar.radio("Navigate", ["Dashboard"])
    if page == "Dashboard":
        show_dashboard()
    # Additional pages can be added here.
