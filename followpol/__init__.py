from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from followpol.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'admin.adminlogin'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from followpol.admin.routes import admin
    from followpol.main.routes import main
    from followpol.errors.handlers import errors
    app.register_blueprint(admin)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app