# trust_score.py
def calculate_trust_score(user_data):
     """
    Calculate the credit score based on earned badges and course completions.
    
    Parameters:
      - user_badges (list): A list of badges the user has earned.
      - course_points (int): Points earned by completing courses.
      - should also call to the AI model to get the base line score
    
    Returns:
      - score (int): The computed credit score.
    """
    # Define point values for each badge
    badge_points = {
        '5-Day Savings Streak': 50,
        '10-Day Savings Streak': 100,
        'Savings Goal Achiever': 150
    }
    
    score = course_points  # Start with points from course completions
    
    # Add points from each badge the user has
    for badge in user_badges:
        score += badge_points.get(badge, 0)
    
    return score