from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "WAPA2025PODER")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "TU_ACCESS_TOKEN_DE_META")

@app.route("/", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == VERIFY_TOKEN:
        return challenge
    return "Invalid verification token", 403

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Mensaje recibido:", data)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
