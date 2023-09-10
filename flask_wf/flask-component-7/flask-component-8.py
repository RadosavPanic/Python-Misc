from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("enter_cookie.html")


@app.route("/error/<message>")
def error(message):
    return f"<h2>Error: {message}</h2>"


@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form['nm']
        response = make_response(render_template("read_cookie.html"))
        response.set_cookie("userID", user)
        return response
    else:
        return redirect(url_for("error", message="this form can only be POST"))


@app.route("/getcookie")
def getcookie():
    uid = request.cookies.get("userID")
    return f"<h1>Hey {uid}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
