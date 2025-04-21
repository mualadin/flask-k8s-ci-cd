from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
   # return f"Hello from Flask! ENV: {os.getenv('APP_ENV')}, SECRET: {os.getenv('SECRET_KEY')}"
   return f"<h1>🚀 CI/CD(using argoCD and gut CI  is working!</h1><p>ENV: {os.environ.get('ENV', 'development')}</p><p>SECRET: {os.environ.get('SECRET', 'notset')}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
