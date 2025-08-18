from flask import Flask
import os

app =  Flask(__name__)

@app.route("/")

def hello():
    return f"Hello, welcome to my flask_app"

@app.route("/bye")

def goodbye():
    return f"Goodbye my friend"

@app.route("/hau")

def how_are_you():
    return f"How are you"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5070)