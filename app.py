from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


load_dotenv()

def create_app():

    # App initialization
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        app.db = SQLAlchemy()
        app.db.init_app(app)

        # Create tables if not exists
        import models
        app.db.create_all()
        app.db.session.commit()

        # Register blueprints
        from routes import routes
        app.register_blueprint(routes)

        if __name__ == '__main__':
            create_app().run()

        return app


