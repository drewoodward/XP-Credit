import streamlit as st
import requests

# Define your Flask API URL
API_URL = "http://127.0.0.1:5000"

def get_credit_score(user_id):
    response = requests.get(f"{API_URL}/credit_score?user_id={user_id}")
    if response.status_code == 200:
        return response.json().get("credit_score")
    else:
        return "Error fetching score"

def main():
    st.title("Gamified Financial Trust Score Dashboard")
    
    user_id = st.text_input("Enter User ID:")
    if st.button("Get Credit Score"):
        if user_id:
            score = get_credit_score(user_id)
            st.write(f"User {user_id} has a credit score of: {score}")
        else:
            st.error("Please enter a valid user ID.")

if __name__ == "__main__":
    main()
