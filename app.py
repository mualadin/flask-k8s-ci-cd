from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from Flask! ENV: {os.getenv('APP_ENV')}, SECRET: {os.getenv('SECRET_KEY')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
