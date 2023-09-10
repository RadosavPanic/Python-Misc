from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base_route():
    return "<h1>Flask base route</h1>"


@app.route("/test/<int:score>")
def show_mark(score):
    return render_template("testgrades.html", marks=score)


if __name__ == "__main__":
    app.run(debug=True)
