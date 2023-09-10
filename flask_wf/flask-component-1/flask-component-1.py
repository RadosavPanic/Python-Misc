from flask import Flask

app = Flask(__name__)


@app.route("/")
def base_route():
    return "Flask base route"


@app.route("/peugeot")
def ford():
    return "<h1>Peugeot</h1>"


@app.route("/profile/<username>")
def profile(username):
    return f"<h1>Hey {username.capitalize()}</h1>"


@app.route("/post/<int:post_id>")
def show_id(post_id):
    return "<h1>ID: {}</h1>".format(post_id)


if __name__ == "__main__":
    app.run()
