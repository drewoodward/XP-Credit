import streamlit as st
from auth import login_signup
from navbar import show_navbar

# Initialize session state attributes
if 'username' not in st.session_state:
    st.session_state['username'] = 'Guest'  # You can replace 'Guest' with any default value

main_background = """
<style>
 .stApp {
    background: linear-gradient(to bottom, #F8F4FF,#EFDECD);
 }
</style>
"""
show_navbar()
st.markdown(main_background, unsafe_allow_html=True)

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
