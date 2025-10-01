import requests
import json

def get_leetcode_solved(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    try:
        r = requests.get(url, timeout=10).json()
        return r.get("totalSolved", 0)
    except Exception:
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
