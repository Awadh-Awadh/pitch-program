from flask import Flask
from config import config_options

app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(config_options[config_name])

    #registering Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app