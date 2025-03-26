import streamlit as st
from dashboard import show_dashboard
from profile import show_profile
from education import show_education
from community import show_community

def show_navbar():
    # Sidebar navigation using a radio button for page selection.
    button = st.sidebar.radio("Navigate", ["Dashboard", "Profile", "Education", "Community"])
    
    if button == "Dashboard":
        show_dashboard()
    elif button == "Profile":
        show_profile()
    elif button == "Education":
        show_education()
    elif button == "Community":
        show_community()
