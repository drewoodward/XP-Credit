import streamlit as st
import pandas as pd
import os
from datetime import datetime
from api import get_credit_score, get_badges, get_trust_history, get_image_as_base64

def show_profile():
    st.header("Profile")
    
    # Display username.
    username = st.session_state.get("username", "Guest")
    st.subheader(f"Username: {username}")
    
    # Display avatar.
    # Update the path below to point to your actual avatar image if available.
    # avatar_path = "avatars/default.png"
    # try:
    #     avatar_image = get_image_as_base64(avatar_path)
    #     avatar_html = f'''
    #         <div style="text-align: center;">
    #             <img src="data:image/png;base64,{avatar_image}" 
    #                  style="height: 100px; width: 100px; border-radius: 50%;">
    #         </div>
    #     '''
    #     st.markdown(avatar_html, unsafe_allow_html=True)
    # except Exception as e:
    #     st.error("Error loading avatar image.")
    
    # Display current trust score.
    trust_score = get_credit_score(username)
    if trust_score is not None:
        st.metric("Current Trust Score", trust_score)
    else:
        st.write("Error fetching trust score.")
    
    # Display badges for Saving Streak
    #st.markdown("<div class='subheader'>Saving Streak, +5 Trust Score Points!</div>", unsafe_allow_html=True)
        
                        ####Trying to find the badges####

    # Load the external Badges
    
    badges_path = os.path.join(os.getcwd(), "src", "frontend","badges","badge1.png")
    print("Current file: ", os.path.join(os.getcwd(), "src", "frontend","badges","badge1.png"))    # debugging
    
                        ### Badge Section ###

    badges = get_badges(st.session_state.username)
    print("Badges")
    print(badges)

    # Display badges header with achievement award image
    achievement_image_path = "src/frontend/badges/achievement-award.png"
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

    if badges:
        cols = st.columns(len(badges))
        for idx, col in enumerate(cols):
            with col:
                st.image(badges[idx], width=100)
                st.markdown("<div style='color:#2980B9; font-size:1em; font-weight:bold;'>Saving Streak, +5 XP!</div>", unsafe_allow_html=True)
    else:
        st.write("No badges earned yet.")
    # Display badges for Course Completed
    #st.markdown("<div class='subheader'>Course Completed, +5 Trust Score Points!</div>", unsafe_allow_html=True)
    if badges:
        cols = st.columns(len(badges))
        for idx, col in enumerate(cols):
            with col:
                st.image(badges[idx], width=100)
                st.markdown("<div style='color:#2980B9; font-size:1em; font-weight:bold;'>Course Completed, +5 Trust Score Points!</div>", unsafe_allow_html=True)
    else:
        st.write("No course completion badges earned yet.")
    
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
