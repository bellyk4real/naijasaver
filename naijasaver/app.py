from flask import Flask

from naijasaver.blueprints.user import user
from naijasaver.extensions import (
    db
)

def create_app(settings_override=None):
    """
    Create a flask application using the app factory pattern
    
    :return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(user)
    extensions(app)

    return app

def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)

    return None