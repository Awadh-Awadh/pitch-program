from flask import Flask
from config import config_options

app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(config_options[config_name])

    #registering the main Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Register authentication Blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app