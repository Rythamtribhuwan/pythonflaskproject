
from flask import Flask
import logging

app = Flask(__name__)

# Disable Flask/Werkzeug request logs
logging.getLogger("werkzeug").disabled = True

@app.route("/")
def home():
    return "Hello Ridam"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

