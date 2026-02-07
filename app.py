# medium-5-bulk-credits/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

credits = {}

@app.route("/health")
def health():
    return "ok"

@app.route("/referral", methods=["POST"])
def referral():
    user = request.json["user"]
    invited = request.json["invited"]

    # BUG: no self / multi-account protection
    credits[user] = credits.get(user,0)+100

    if credits[user] >= 1000:
        return jsonify({"credits":credits[user],"flag":FLAG})

    return jsonify({"credits":credits[user]})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
