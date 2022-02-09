# root/3_customer_service/restaurant_application/__init__.py

# TODO typing implementation
import os, config
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Initialize db and login_manager plugins for our flask app
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """
    This method is used to register the flask blueprints and return app object
    :return: <Flask> app object
    """
    # initialize Flask object
    app = Flask(__name__)
    # environment configuration
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # import blueprint
        from .restaurant_api import r_api_blueprint
        # register to app object
        app.register_blueprint(r_api_blueprint)
        return app
