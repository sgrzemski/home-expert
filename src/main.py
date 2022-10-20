from flask import Flask

app = Flask(__name__)


@app.route('/liveness')
def liveness_probe():
    return "OK"


@app.route('/readiness')
def readiness_probe():
    return "OK"


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
