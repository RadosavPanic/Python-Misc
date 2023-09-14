import os
import random
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = ["txt", "pdf", "png", "jpg", "jpeg", "gif"]

app = Flask(__name__)

lstr = list("interesting")
random.shuffle(lstr)
app.secret_key = str(lstr)
app.config["UPLOAD_FOLDER"] = "./uploadfiles/"
app.config["MAX_CONTENT_LENGTH"] = 10*1024*1024


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload")
def upload_file():
    return render_template("uploadfile.html")


@app.route("/uploader", methods=["POST"])
def uploader():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(url_for("upload_file"))
        f = request.files["file"]
        if f.filename == "":
            flash("No selected file")
            return redirect(url_for("upload_file"))
        if allowed_file(f.filename):
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(f.filename)))
            return "File uploaded successfully"
        else:
            flash("File extension is not allowed")
            return redirect(url_for("upload_file"))


if __name__ == "__main__":
    app.run(debug=True)

