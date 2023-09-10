from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base_route():
    return "<h1>Flask base route</h1>"


@app.route("/test/<int:score>")
def show_mark(score):
    return render_template("testgrades.html", marks=score)


@app.route("/profile/<name>")
def pass_name(name):
    return render_template("profile.html", name_param=name.capitalize())


@app.route("/results")
def result():
    dictResults = {'physics': 50, 'chemistry': 60, 'maths': 80}
    return render_template("results.html", result=dictResults)


if __name__ == "__main__":
    app.run(debug=True)
