import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
    DEBUG = True



class ProdConfig(Config):

    pass


config_options = {
  'developmenent':DevConfig,
  'production':ProdConfig
}