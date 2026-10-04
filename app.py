from flask import Flask
import logging

app = Flask(__name__)

logging.getLogger("werkzeug").disabled = True

@app.route("/")
def home():
    return "Rytham - Flask Jenkins Deployment Successfully Completed!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
