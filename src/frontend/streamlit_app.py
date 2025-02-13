import streamlit as st
import pandas as pd
import requests

# Define your Flask API base URL
API_URL = "http://127.0.0.1:5000"

def get_credit_score(user_id):
    """
    Call the Flask API to get the current trust score for a given user.
    """
    response = requests.get(f"{API_URL}/credit_score?user_id={user_id}")
    if response.status_code == 200:
        return response.json().get("credit_score")
    else:
        return "Error fetching score"

def get_trust_history(user_id):
    """
    Call the Flask API to get historical trust score data for the past year.
    Expects a JSON response with a list of records containing 'date' and 'trust_score'.
    """
    response = requests.get(f"{API_URL}/trust_history?user_id={user_id}")
    if response.status_code == 200:
        data = response.json()
        if data:  # Check if data is not empty
            df = pd.DataFrame(data)
            # Convert the date column to datetime if necessary
            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                df = df.sort_values(by='date')
            return df
    return None

def main():
    st.title("Gamified Financial Trust Score Dashboard")
    
    # Input field for the user ID
    user_id = st.text_input("Enter User ID:")

    if user_id:
        # Get the current trust score and display it
        score = get_credit_score(user_id)
        st.metric("Current Trust Score", score)
        
        # Fetch historical trust score data
        df_history = get_trust_history(user_id)
        if df_history is not None and not df_history.empty:
            st.subheader("Trust Score History (Past Year)")
            # Display the data as a table for reference
            st.write(df_history.head())
            # Plot the trust score history using a line chart
            # Assume that 'date' is the x-axis and 'trust_score' is the y-axis.
            st.line_chart(df_history.set_index('date')['trust_score'])
        else:
            st.write("No historical trust score data available for this user.")
    else:
        st.write("Please enter a valid user ID to view trust score information.")

if __name__ == "__main__":
    main()
