from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def base_route():
    return "<h1>Flask base route</h1>"


@app.route("/success/<name>")
def success(name):
    return (f"<p>Login successful!</p>"
            f"<p>Welcome {name}</p>")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for("success", name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for("success", name=user))


if __name__ == "__main__":
    app.run(debug=True)
