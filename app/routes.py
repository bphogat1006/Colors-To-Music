from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import app
from werkzeug.utils import secure_filename
import os

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/uploader", methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        image = request.files['image']
        if image.filename == '':
            print('No image selected')
            return redirect("/home")
        filename = secure_filename(image.filename)
        fileExtension = filename.split(".")[1]
        if fileExtension not in app.config["ALLOWED_EXTENSIONS"]:
            print('image file type "'+fileExtension+'" not supported')
            return redirect("/home")
        path = os.path.join(app.root_path, app.config["IMAGE_UPLOADS_PATH"], filename)
        image.save(path)
        return render_template("display.html", filename="uploads/"+filename)

