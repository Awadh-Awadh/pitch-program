from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from config import config_options
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    #registering the main Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Register authentication Blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
    #initializing bootstrap
    bootstrap.init_app(app)
    # initializing SQLAlchemy
    db.init_app(app)

    return app