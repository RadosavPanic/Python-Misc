from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def base_route():
    return "<h1>Flask base route</h1>"


@app.route("/admin")
def adminProfile():
    return "Welcome back Admin"


@app.route("/guest/<guestname>")
def guestProfile(guestname):
    return f"Welcome back {guestname} as Guest"


@app.route("/user/<name>")
def userProfileRedirect(name):
    if name == "admin":
        return redirect(url_for("adminProfile"))
    else:
        return redirect(url_for("guestProfile", guestname=name))


if __name__ == "__main__":
    app.run(debug=True)
