# app.py
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def sensor():
    return {
        "speed": random.randint(40,120),
        "temperature": random.randint(30,90),
        "status": "OK"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
