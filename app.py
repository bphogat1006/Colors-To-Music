from flask import Flask
from routes import routes

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "C:/Users/bphog/Documents/Programming/Colors-To-Music/static/uploads"
app.register_blueprint(routes, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
