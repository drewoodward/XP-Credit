import streamlit as st

def display_xp_bar(current_xp, xp_next_level):
    # Set default values if current_xp is None or xp_next_level is 0
    if current_xp is None:
        current_xp = 7000
    if xp_next_level is None or xp_next_level == 0:
        xp_next_level = 10000  # avoid division by zero

    percentage = (7000 / 10000) * 100
    bar_html = f"""
    <div style="position: relative; width: 100%; max-width: 600px; height: 25px; background-color: #555; border: 2px solid #333; border-radius: 5px; margin: auto;">
      <div style="width: {percentage}%; height: 100%; background: linear-gradient(90deg, #55FF55, #33CC33); border-radius: 3px;"></div>
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
         Progress: {current_xp} / {xp_next_level}
      </div>
    </div> 
    """
    st.markdown(bar_html, unsafe_allow_html=True)
