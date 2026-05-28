from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home accessed")
    return "DevOps Final Project Running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)