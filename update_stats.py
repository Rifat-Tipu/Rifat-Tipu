import requests
import json

def get_leetcode_solved(username):
    url = f"https://alfa-leetcode-api.onrender.com/{username}/solved"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()

        # API returns {"solvedProblem": 150, ...}
        return data.get("solvedProblem", 0)

    except Exception as e:
        print(f"Error fetching LeetCode stats: {e}")
        return 0


leetcode_username = "vampire_77"

leetcode_stats = {
    "schemaVersion": 1,
    "label": "LeetCode",
    "message": f"{get_leetcode_solved(leetcode_username)} problems",
    "color": "E05D44"
}

with open("lc.json", "w") as f:
    json.dump(leetcode_stats, f)
