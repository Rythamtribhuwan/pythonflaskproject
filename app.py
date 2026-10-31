from flask import Flask
import logging

app = Flask(__name__)

logging.getLogger("werkzeug").disabled = True

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Python Jenkins Project</title>
    </head>
    <body>
        <h1>Welcome to Python Project</h1>
        <h2>Jenkins Deployment</h2>
        <p>Flask Application Successfully Deployed!</p>
        <h2>Version 1.0.0</h2>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
