from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from script.config import Config
import psycopg2

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    bcrypt.init_app(app)
    login_manager.init_app(app)
    from script.users.routes import users
    from script.posts.routes import posts
    from script.messages.routes import messages
    from script.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(messages)
    app.register_blueprint(main)
    from script.errors.handlers import errors 
    app.register_blueprint(errors)

    return app