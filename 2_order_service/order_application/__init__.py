# root/2_order_service/order_application/__init__.py
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
    environment_configuration = os.environ["CONFIGURATION_SETUP"]
    app.config.from_object(environment_configuration)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # import blueprint
        from .order_api import o_api_blueprint

        # register to app object
        app.register_blueprint(o_api_blueprint)
        return app
