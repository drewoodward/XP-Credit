import streamlit as st
import random
import requests
import base64
import pandas as pd
from api import (
    get_credit_score, 
    get_trust_history, 
    update_trust_score, 
    get_badges, 
    get_image_as_base64
)

def show_dashboard():
    st.markdown(f"<div class='header'>Welcome, {st.session_state.username}!</div>", unsafe_allow_html=True)
    
    # Display current trust score
    score = get_credit_score(st.session_state.username)
    if score is not None:
        st.metric("Current Trust Score", score)
    else:
        st.write("Error fetching trust score.")
    
    # Simulated bank linking section
    st.markdown("<div class='subheader'>Link Your Bank Account</div>", unsafe_allow_html=True)
    st.write("Click the button below to log into your bank via Plaid (simulation).")
    if st.button("Link Bank Account"):
        st.success("Bank account linked successfully!")
        new_trust_score = random.randint(600, 800)
        _, status = update_trust_score(st.session_state.username, new_trust_score)
        if status == 200:
            st.success("Trust score updated!")
        else:
            st.error("Failed to update trust score.")
    
    # Display historical trust score data and graph
    st.markdown("<div class='subheader'>Trust Score History (Past Year)</div>", unsafe_allow_html=True)
    df_history = get_trust_history(st.session_state.username)
    if df_history is not None and not df_history.empty:
        st.write("Historical Data Preview:")
        st.write(df_history.head())
        if 'date' in df_history.columns:
            st.line_chart(df_history.set_index('date')['trust_score'])
        elif 'timestamp' in df_history.columns:
            st.line_chart(df_history.set_index('timestamp')['trust_score'])
    else:
        st.write("No historical trust score data available.")
    
    # Display badges header with achievement award image
    achievement_image_path = "badges/achievement-award.png"
    try:
        encoded_image = get_image_as_base64(achievement_image_path)
    except Exception as e:
        st.error(f"Error loading achievement image: {e}")
        encoded_image = ""
    
    image_html = f'<img src="data:image/png;base64,{encoded_image}" style="height: 50px; margin-left: 10px;">'
    st.markdown(f"""
        <div class='subheader' style='display: flex; align-items: center; justify-content: center;'>
            Your Badges {image_html}
        </div>
    """, unsafe_allow_html=True)
    
    # Display badges for Saving Streak
    st.markdown("<div class='subheader'>Saving Streak, +5 Trust Score Points!</div>", unsafe_allow_html=True)
    badges = get_badges(st.session_state.username)
    if badges:
        cols = st.columns(len(badges))
        for idx, col in enumerate(cols):
            with col:
                st.image(badges[idx], width=100)
                st.markdown("<div style='color:#2980B9; font-size:1em; font-weight:bold;'>Saving Streak, +5 Trust Score Points!</div>", unsafe_allow_html=True)
    else:
        st.write("No badges earned yet.")
    
    # Display badges for Course Completed
    st.markdown("<div class='subheader'>Course Completed, +5 Trust Score Points!</div>", unsafe_allow_html=True)
    if badges:
        cols = st.columns(len(badges))
        for idx, col in enumerate(cols):
            with col:
                st.image(badges[idx], width=100)
                st.markdown("<div style='color:#2980B9; font-size:1em; font-weight:bold;'>Course Completed, +5 Trust Score Points!</div>", unsafe_allow_html=True)
    else:
        st.write("No course completion badges earned yet.")
