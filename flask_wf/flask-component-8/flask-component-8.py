from flask import Flask, session, request, redirect, url_for
import random

app = Flask(__name__)

lstr = list("interesting")
print(lstr)  # ['i', 'n', 't', 'e', 'r', 'e', 's', 't', 'i', 'n', 'g']
random.shuffle(lstr)
print(lstr)  # ['e', 'e', 'g', 't', 's', 'n', 'n', 'i', 'i', 't', 'r'] (random shuffled elements)
app.secret_key = str(lstr)


@app.route("/")
def index():
    if "username" in session:
        username = session['username']
        return f"""Logged in as {username} <br>
                   <strong><a href='/logout'>Click here to log out</a></strong>"""
    return "You are not logged in <br><a href='/login'><strong>Click here to log in</strong></a>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for("index"))
    return """
    <form method="post">
        <p><input type="text" name="username"/></p>
        <p><input type="submit" value="Login"/></p>
    </form>"""


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
