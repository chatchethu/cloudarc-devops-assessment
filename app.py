import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/", methods=["GET"])
def home():
    app.logger.info("Homepage requested")
    return jsonify({
        "application": "CloudArc DevOps Demo",
        "status": "running",
        "environment": APP_ENV
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
