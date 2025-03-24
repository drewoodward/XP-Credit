import streamlit as st
from xp import display_xp_bar

def show_community():
    st.header("Community")
    st.write("Welcome to our Community page!")
    st.markdown("Our goal is to build a social platform where users can talk, share, and compare badges—just like on Twitter. For now, join our communal Discord server to connect with others!")
    st.markdown("[Join our Discord Server](https://discord.gg/PVHMzCGx)")

    st.write("\n")
    


    st.subheader("This Weeks Community Challenge!")
    st.write("In this weeks challenge, users are collectively trying to save $10,000.")
    
    # Display xp
    # current_xp =  get_user_xp(st.session_state.username) # Example: the user currently has 120 XP
    # if current_xp is None:
    #     current_xp = 0
    current_xp = str("7,500")    # Hard-coded amount to
    xp_next_level = str("10,000")  # Example: the next level is reached at 200 XP
    
    display_xp_bar(current_xp, xp_next_level)
    
    st.write("\n")
    st.write("\n")
    
    if st.button("Join Challenge", key="green"): 
            st.success("You are enrolled to this weeks challenge!")