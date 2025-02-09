# gamification.py

import requests

# Define available badges and we need like 10 more
BADGES = {
    'streak_5': '5-Day Savings Streak',
    'streak_10': '10-Day Savings Streak',
    'savings_goal': 'Savings Goal Achiever'
}

def assign_badge(user_id, event_type, **kwargs):
    """
    Assign a badge to a user based on the event type.
    
    Parameters:
      - user_id (int): The identifier for the user.
      - event_type (str): Type of event. Can be 'streak' or 'savings_goal'.
      - kwargs: Additional parameters needed for the specific event.
          For a 'streak', include: streak_count (int)
          For a 'savings_goal', include: goal_amount (float) and savings_amount (float)
          
    Returns:
      - badge (str) if criteria are met, or None if no badge is assigned.
    """
    badge = None

    if event_type == 'streak':
        streak_count = kwargs.get('streak_count', 0)
        if streak_count >= 10:
            badge = BADGES.get('streak_10')
        elif streak_count >= 5:
            badge = BADGES.get('streak_5')

    elif event_type == 'savings_goal':
        goal_amount = kwargs.get('goal_amount', 0)
        savings_amount = kwargs.get('savings_amount', 0)
        if savings_amount >= goal_amount:
            badge = BADGES.get('savings_goal')

    # If a badge is assigned, we simulate an external action via a public API.
    if badge:
        try:
            # This is a placeholder public API call (using a public API directory as an example).
            # In your actual project, you might integrate with a social sharing API,
            # a logging service, or another third-party API.
            response = requests.get('https://api.publicapis.org/entries')
            if response.status_code == 200:
                print("Successfully called public API to log badge assignment.")
            else:
                print("Public API call did not return a success status.")
        except Exception as e:
            print(f"Public API call encountered an error: {e}")
    
    return badge


# Example usage for testing
if __name__ == '__main__':
    # Simulate a user hitting a savings streak
    user_id = 101
    streak_badge = assign_badge(user_id, 'streak', streak_count=7)
    if streak_badge:
        print(f"User {user_id} earned a badge: {streak_badge}")
    else:
        print(f"User {user_id} did not qualify for a streak badge.")

    # Simulate a user reaching their savings goal
    savings_badge = assign_badge(user_id, 'savings_goal', goal_amount=1000.0, savings_amount=1200.0)
    if savings_badge:
        print(f"User {user_id} earned a badge: {savings_badge}")
    else:
        print(f"User {user_id} did not meet the savings goal for a badge.")
