import os

os.environ['DATABASE_URL'] = postgres://ftywwlawtrzyfg:ec8163dc63c7ed95af1c707525adb5fd234dd88a7331a393c6995e31efd9a2ef@ec2-176-34-114-78.eu-west-1.compute.amazonaws.com:5432/dekiit0jntesar

class Config:
    SECRET_KEY = '4ed80220c43e95bc68fccd65816fa731'
    DATABASE_URL = os.environ['DATABASE_URL']