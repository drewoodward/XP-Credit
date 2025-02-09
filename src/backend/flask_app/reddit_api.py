import praw

def reddit_auth():
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        username='YOUR_REDDIT_USERNAME',
        password='YOUR_REDDIT_PASSWORD',
        user_agent='gamified_credit:v1.0 (by /u/YOUR_REDDIT_USERNAME)'
    )
    return reddit

def post_credit_score(reddit, subreddit_name, user_id, credit_score):
    title = f"User {user_id} Credit Score Update"
    body = f"Congratulations! Based on your achievements, your current credit score is **{credit_score}**."
    submission = reddit.subreddit(subreddit_name).submit(title, selftext=body)
    return submission

# Example integration
if __name__ == '__main__':
    # Example data
    user_id = 101
    user_badges = ['10-Day Savings Streak', 'Savings Goal Achiever']
    course_points = 200

    # Calculate the credit score
    credit_score = calculate_credit_score(user_badges, course_points)
    print(f"Calculated Credit Score: {credit_score}")

    # Post the score to Reddit
    reddit = reddit_auth()
    submission = post_credit_score(reddit, 'your_dedicated_subreddit', user_id, credit_score)
    print("Posted to Reddit:", submission.url)
