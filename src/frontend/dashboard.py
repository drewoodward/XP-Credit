import streamlit as st
import random
import requests
import base64
import pandas as pd
import os
from xp import display_xp_bar
from api import (
    get_credit_score, 
    get_trust_history, 
    update_trust_score, 
    get_badges, 
    get_image_as_base64,
    get_user_xp
)
import pathlib


# Function to load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load the external CSS
css_path = os.path.join("frontend","assets","styles.css")
print(os.getcwd())
load_css(css_path)


def show_dashboard():
    #old version without streamlit --upgrade
    #st.markdown(f"<div class='header'>Welcome, {st.session_state.username}!</div>", unsafe_allow_html=True)
    st.title("✨ Welcome, " + st.session_state.username + "! ✨")
    
    st.write(" \n")
    
    # Display xp
    # current_xp =  get_user_xp(st.session_state.username) # Example: the user currently has 120 XP
    # if current_xp is None:
    #     current_xp = 0
    current_xp = 120    # Hard-coded amount to
    xp_next_level = 200  # Example: the next level is reached at 200 XP
    
    display_xp_bar(current_xp, xp_next_level)

    # Display current trust score
    score = get_credit_score(st.session_state.username)
    if score is not None:
        st.header("Current Trust Score")
        st.subheader(score)
        st.write(" \n") 
    else:
        st.write("Error fetching trust score.")
    
    # Simulated bank linking section
    if st.button("Link Bank Account", key="pulse"): 
        st.success("Bank account linked successfully!")
        new_trust_score = random.randint(600, 800)
        _, status = update_trust_score(st.session_state.username, new_trust_score)
        if status == 200:
            st.success("Trust score updated!")
        else:
            st.error("Failed to update trust score.")
    
    # Display historical trust score data and graph with a date range filter
    st.subheader("Trust Score History")
    df_history = get_trust_history(st.session_state.username)
    if df_history is not None and not df_history.empty:
        st.write("Historical Data Preview:")
        st.write(df_history.head())
        
        # Assume the date field is named 'date'
        if 'date' in df_history.columns:
            # Convert to datetime if not already done
            df_history['date'] = pd.to_datetime(df_history['date'], errors='coerce')
            df_history = df_history.sort_values(by='date')
            
            # Add a date range filter widget
            min_date = df_history['date'].min().date()
            max_date = df_history['date'].max().date()
            date_range = st.date_input("Select date range", value=[min_date, max_date])
            if len(date_range) == 2:
                start_date, end_date = date_range
                mask = (df_history['date'].dt.date >= start_date) & (df_history['date'].dt.date <= end_date)
                filtered_df = df_history.loc[mask]
            else:
                filtered_df = df_history

            st.line_chart(filtered_df.set_index('date')['trust_score'])
        elif 'timestamp' in df_history.columns:
            df_history['timestamp'] = pd.to_datetime(df_history['timestamp'], errors='coerce')
            df_history = df_history.sort_values(by='timestamp')
            st.line_chart(df_history.set_index('timestamp')['trust_score'])
    else:
        st.write("No historical trust score data available.")
    
    
    
    
