# medium-5-bulk-credits/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

credits = {}

@app.route("/")
def index():
    return """
<h2>Referral Credits Platform</h2>
<ul>
<li>POST /referral</li>
<li>GET /health</li>
</ul>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/referral", methods=["POST"])
def referral():
    user = request.json["user"]
    invited = request.json["invited"]

    credits[user] = credits.get(user,0)+100

    if credits[user] >= 1000:
        return jsonify({"credits":credits[user],"flag":FLAG})

    return jsonify({"credits":credits[user]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
