import os
from flask import Flask

app =  Flask(__name__)

@app.route("/")

def hello():
    return f"Hello, welcome to my flask_app"

@app.route("/bye")

def goodbye():
    return f"Goodbye my friend"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)