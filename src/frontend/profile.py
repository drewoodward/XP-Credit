import streamlit as st
import pandas as pd
from datetime import datetime
from api import get_credit_score, get_badges, get_trust_history, get_image_as_base64

def show_profile():
    st.header("Profile")
    
    # Display username.
    username = st.session_state.get("username", "Guest")
    st.subheader(f"Username: {username}")
    
    # Display avatar.
    # Update the path below to point to your actual avatar image if available.
    avatar_path = "avatars/default.png"
    try:
        avatar_image = get_image_as_base64(avatar_path)
        avatar_html = f'''
            <div style="text-align: center;">
                <img src="data:image/png;base64,{avatar_image}" 
                     style="height: 100px; width: 100px; border-radius: 50%;">
            </div>
        '''
        st.markdown(avatar_html, unsafe_allow_html=True)
    except Exception as e:
        st.error("Error loading avatar image.")
    
    # Display current trust score.
    trust_score = get_credit_score(username)
    if trust_score is not None:
        st.metric("Current Trust Score", trust_score)
    else:
        st.write("Error fetching trust score.")
    
    # Display badges earned.
    st.subheader("Badges Earned")
    badges = get_badges(username)
    if badges:
        cols = st.columns(len(badges))
        for idx, col in enumerate(cols):
            with col:
                st.image(badges[idx], width=80)
    else:
        st.write("No badges earned yet.")
    
    # Display last activity (using trust history).
    st.subheader("Last Activity")
    df_history = get_trust_history(username)
    last_activity = None
    if df_history is not None and not df_history.empty:
        if 'date' in df_history.columns:
            df_history['date'] = pd.to_datetime(df_history['date'], errors='coerce')
            last_activity = df_history['date'].max()
        elif 'timestamp' in df_history.columns:
            df_history['timestamp'] = pd.to_datetime(df_history['timestamp'], errors='coerce')
            last_activity = df_history['timestamp'].max()
    
    if last_activity:
        # Format the datetime as desired.
        st.write("Last Activity:", last_activity.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        st.write("No recent activity recorded.")
