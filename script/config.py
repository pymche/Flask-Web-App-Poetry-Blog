import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgres://ftywwlawtrzyfg:ec8163dc63c7ed95af1c707525adb5fd234dd88a7331a393c6995e31efd9a2ef@ec2-176-34-114-78.eu-west-1.compute.amazonaws.com:5432/dekiit0jntesar'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')