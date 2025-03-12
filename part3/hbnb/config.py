import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevelopmentConfig(Config):
    DEBUG = True
    

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}