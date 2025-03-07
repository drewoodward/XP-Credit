# gamified-credit
A web-based platform that evaluates financial trustworthiness through AI-driven insights while incentivizing responsible financial behaviors.

Purpose: Traditional credit scoring systems often penalize financial missteps and fail to reward proactive financial responsibility. Our project reimagines this model by leveraging behavioral psychology—specifically the IKEA Effect and Self-Determination Theory—and gamification principles to create an engaging, positive, and empowering financial experience.

# Technologies Used:
    Backend: Flask
    Frontend: Streamlit
    AI/ML: PyTorch
    Database: Firestore
    Authentication: Firebase Auth


# Dependencies
Flask: pip install Flask
Firebase Admin: pip install firebase_admin
Streamlit: pip install streamlit
PyTorch: Installation instructions available at PyTorch.org
Additional Python dependencies as listed in requirements.txt

# How to use
1.Create a Virtual Environment:
python3 -m venv env

2.Install Dependencies:
pip install -r requirements.txt

Or install individual packages:
pip install Flask firebase_admin streamlit

3.Firebase Configuration:
Create a JSON file containing your Firebase credentials.
Ensure the file is placed in the expected directory (as referenced in your Flask app).

# Running the Application
Start the Flask Backend:

Set the Flask app environment variable:
export FLASK_APP=path/to/flask_app

Run the Flask application:
flask run

Launch the Streamlit Frontend:

In a separate terminal, navigate to your Streamlit app directory and run:
streamlit run streamlit_app.py

When prompted, enter your email and open the provided URL in your browser.

# Features
Financial Trust Score Model:
Evaluates trustworthiness using AI-driven insights beyond traditional credit metrics.

Gamification System for Financial Literacy:
Engages users with interactive challenges, streaks, leaderboards, and courses to reward responsible financial behavior.

Community Engagement:
Built using Flask, Firestore, and Streamlit, the platform fosters a supportive environment for financial growth.

# AI Model Details
The AI component is built using PyTorch and comprises four key phases:

1. Synthetic Data Generation:
Generates realistic financial datasets using the Faker library.
Assigns financial scores based on weighted financial behaviors.

2. Preprocessing & Training:
Utilizes StandardScaler for data normalization.
Trains a three-layer fully connected neural network with ReLU activations.
Optimized using the Adam optimizer and Mean Squared Error loss.

3. Prediction & Evaluation:
Evaluates model performance using test datasets.
Generates financial trustworthiness scores from input features.

4. Integration:
The trained model is served via a Flask API.
Firestore stores user financial behavior data for continuous refinement.
Streamlit provides an intuitive frontend for user interaction.

# Gamification Strategy
Inspired by platforms like Duolingo and Robinhood, our gamification approach includes:

Challenges, Streaks & Courses:
Users complete financial tasks (e.g., budgeting, debt management) to earn points and improve their trust score.

Leaderboards & Community Features:
Public leaderboards and badges encourage friendly competition and community engagement.

Behavioral Psychology:
    Positive Reinforcement: Rewards for proactive financial behavior.
    Self-Determination Theory: Fosters autonomy, competence, and relatedness.
    The IKEA Effect: Empowers users by having them "build" their financial profiles.

# Future Enhancements
Feature Engineering:
Incorporate additional financial behavior metrics such as rent payments, utility bills, and alternative credit indicators.

Model Optimization:
Experiment with advanced architectures (LSTMs, transformers) and regularization to enhance model performance.

Bias & Fairness Audits:
Implement explainable AI (XAI) techniques to ensure transparency and fairness in financial assessments.

Scalability:
Develop an online learning framework for continuous model updates based on real-world data.

Integration of LLMs:
Leverage large language models to offer personalized financial advice.

Mobile & Web Integration:
Expand accessibility with dedicated mobile applications and enhanced web interfaces.

# Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Open a pull request with a detailed explanation of your changes.
