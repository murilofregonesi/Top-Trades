from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


load_dotenv()
db = SQLAlchemy()

def create_app():

    # App initialization
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    @app.route("/")
    def home():
        # TODO Update home function and location
        posts = [1, 2]
        return render_template("blog.html", posts=posts)

    with app.app_context():
        db.init_app(app)

        # Create tables if not exists
        import models
        db.create_all()
        db.session.commit()
        
        # TODO Register routes

        if __name__ == '__main__':
            create_app().run()

        return app


