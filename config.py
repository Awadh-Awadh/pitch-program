import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard stuff to to crack'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    MAIL_SERVER = 'smtp.google.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class DevConfig(Config):
    DEBUG = True



class ProdConfig(Config):

    pass


config_options = {
  'development':DevConfig,
  'production':ProdConfig
}