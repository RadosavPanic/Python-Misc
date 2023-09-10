from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def base_route():
    return "<h3>Flask base route</h3>"


@app.route("/what", methods=["GET", "POST"])
def what():
    if request.method == "GET":
        return "GET method requested"
    else:
        return "POST method requested"


if __name__ == "__main__":
    app.run()
