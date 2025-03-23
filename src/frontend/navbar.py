import streamlit as st
from dashboard import show_dashboard
from profile import show_profile
from education import show_education
from community import show_community

def show_navbar():
    # Sidebar navigation using a radio button for page selection.
    page = st.sidebar.radio("Navigate", ["Dashboard", "Profile", "Education", "Community"])
    
    if page == "Dashboard":
        show_dashboard()
    elif page == "Profile":
        show_profile()
    elif page == "Education":
        show_education()
    elif page == "Community":
        show_community()
