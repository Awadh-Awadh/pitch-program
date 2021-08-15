import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+pyscopg2://moringa:Access/@localhost/pitch'

class DevConfig(Config):
    DEBUG = True



class ProdConfig(Config):

    pass


config_options = {
  'developmenent':DevConfig,
  'production':ProdConfig
}