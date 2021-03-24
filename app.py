from flask import Flask, render_template
import os
from dotenv import load_dotenv


load_dotenv()

def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    @app.route("/")
    def home():
        posts = [1, 2]
        return render_template("blog.html", posts=posts)

    return app


    