import streamlit as st

def show_education():
    st.header("Education: 50/30/20 Budgeting Rule")
    
    # Article caption and link.
    st.markdown("""
    **Caption:** It is hard to properly budget without understanding the constraints one's fixed expenses can have.  
    Read this article regarding the [50/30/20 budgeting rule](https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp) to get a template on how to balance one's finances!
    """)
    
    st.write("---")
    st.subheader("Quiz: Test Your Knowledge")
    
    # Question 1
    q1 = st.radio(
        "1. What is an appropriate need that must be covered first?",
        ("Tickets to Sporting Events", "Creating an emergency fund", "Minimum debt payments", "Clothing")
    )
    
    # Question 2
    q2 = st.radio(
        "2. What type of income should be used applying the 50/30/20 rule?",
        ("Gross Income (before taxes)", "Net income (after taxes)", "Total Household income before deductions")
    )
    
    # Question 3
    q3 = st.radio(
        "3. Why is the 50/30/20 budget rule considered useful?",
        (
            "It forces people to save aggressively while minimizing all expenses.",
            "It provides a simple structure for balancing essential expenses, financial goals, and lifestyle spending.",
            "It ensures that all discretionary spending is eliminated.",
            "It is required by law for personal finance management."
        )
    )
    
    # Question 4
    q4 = st.radio(
        "4. What length of time does the article mention to be necessary for a proper emergency savings account?",
        ("2 weeks", "1 year", "3 months", "1 month")
    )
    
    # Question 5
    q5 = st.radio(
        "5. If your monthly net income is $4,000, how much should ideally go toward 'wants' under the 50/30/20 rule?",
        ("$1,200", "$2,000", "$800", "$600")
    )
    
    if st.button("Submit Quiz"):
        # Define the correct answers.
        correct_answers = {
            "q1": "Minimum debt payments",
            "q2": "Net income (after taxes)",
            "q3": "It provides a simple structure for balancing essential expenses, financial goals, and lifestyle spending.",
            "q4": "3 months",
            "q5": "$1,200"
        }
        user_answers = {
            "q1": q1,
            "q2": q2,
            "q3": q3,
            "q4": q4,
            "q5": q5
        }
        
        # Calculate the score.
        score = sum(1 for key in correct_answers if correct_answers[key] == user_answers[key])
        total = len(correct_answers)
        
        if score == total:
            st.success(f"Congratulations! You passed the quiz with a score of {score}/{total} and earned a badge!")
            # Optionally, display a badge image:
            # st.image("badges/education_badge.png", width=100)
        else:
            st.error(f"You scored {score}/{total}. Some answers are incorrect. Please try again!")
