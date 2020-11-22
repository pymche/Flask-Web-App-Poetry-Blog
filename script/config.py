import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URL = os.environ['DATABASE_URL']