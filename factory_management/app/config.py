import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')  # Set a strong secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///factory_management.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
