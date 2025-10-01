import requests
import json

def get_leetcode_solved(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    try:
        r = requests.get(url, timeout=10).json()
        return r.get("totalSolved", 0)
    except Exception:
        return 0

def get_codeforces_solved(username):
    url = f"https://codeforces.com/api/user.status?handle={username}"
    try:
        r = requests.get(url, timeout=10).json()
        if r["status"] != "OK":
            return 0
        solved = set()
        for sub in r["result"]:
            if sub.get("verdict") == "OK":
                problem_id = str(sub["problem"].get("contestId", "")) + str(sub["problem"].get("index", ""))
                solved.add(problem_id)
        return len(solved)
    except Exception:
        return 0

leetcode_username = "vampire_77"
codeforces_username = "Rifat777"

stats = {
    "schemaVersion": 1,
    "label": "Problems Solved",
    "message": f"CF {get_codeforces_solved(codeforces_username)} | LC {get_leetcode_solved(leetcode_username)}",
    "color": "00b09b"
}

with open("stats.json", "w") as f:
    json.dump(stats, f)
