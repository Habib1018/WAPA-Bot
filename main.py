from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "WAPA2025PODER"  # Reemplaza si usas otro
ACCESS_TOKEN = "TU_ACCESS_TOKEN_DE_META"

@app.route("/", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == VERIFY_TOKEN:
        return challenge
    return "Error: token inválido", 403

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Mensaje recibido:", data)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
