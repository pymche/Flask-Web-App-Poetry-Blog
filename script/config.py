import os

class Config:
    SECRET_KEY = '4ed80220c43e95bc68fccd65816fa731'
    DATABASE_URL = os.environ['DATABASE_URL']