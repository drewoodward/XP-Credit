import random
import json
import requests
from datetime import datetime, timezone

prev_score = 640  # Start at 640
max_score = 720

# Run 52 iterations (e.g., representing weekly updates for one year)
for i in range(52):
    # Randomly decide whether to increment by 5 (50% chance), 
    # but only if adding 5 doesn't exceed the max_score.
    if random.choice([True, False]) and prev_score + 5 <= max_score:
        trust_score = prev_score + 5
    else:
        trust_score = prev_score

    prev_score = trust_score

    print(f"Predicted Financial Score: {trust_score:.2f}")

    prediction_record = {
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "trust_score": trust_score,
        "username": "testuser"
    }

    prediction_json = json.dumps(prediction_record, indent=4)
    print("Prediction JSON:")
    print(prediction_json)

    response = requests.post("http://127.0.0.1:5000/update_trust_score", json=prediction_record)
    if response.status_code in (200, 201):
        print("Prediction stored successfully!")
    else:
        print("Error storing prediction:", response.text)
