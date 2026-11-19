import sys
sys.path.insert(0, "/var/jenkins_home/python-packages")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Jenkins Multi-Stage Pipeline!"

if __name__ == "__main__":
    app.run(debug=False)
