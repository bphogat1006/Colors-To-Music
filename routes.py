import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename

routes = Blueprint(__name__, "routes")


@routes.route("/")
def home():
    return render_template("index.html")

@routes.route("/uploader", methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        if "image" not in request.files:
            print("'image' not in request.files")
            return redirect("/")
        image = request.files['image']
        if image.filename == '':
            print('No image selected')
            return redirect("/")
        filename = secure_filename(image.filename)
        path = os.path.join(current_app.config["IMAGE_UPLOADS"], filename)
        image.save(path)
        return render_template("index.html", filename="uploads/"+filename)
