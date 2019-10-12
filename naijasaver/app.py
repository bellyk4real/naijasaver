from flask import Flask

from naijasaver.blueprints.user import user

def create_app():
    """
    Create a flask application using the app factory pattern
    
    :return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('setting.py', silent=True)

    app.register_blueprint(user)
    return app