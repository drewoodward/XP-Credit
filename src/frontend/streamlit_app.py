import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

    #from github.com/techwithtim/Streamlit-Intro-App
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        st.write(df.head())

        st.subheader("Data Summary")
        st.write(df.describe())

        st.subheader("Filter Data")
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select column to filter by", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("Select value", unique_values)

        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

        st.subheader("Plot Data")
        x_column = st.selectbox("Select x-axis column", columns)
        y_column = st.selectbox("Select y-axis column", columns)

        if st.button("Generate Plot"):
            st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting on file upload...")




if __name__ == "__main__":
    main()
