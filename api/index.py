"""App's entrypoint file."""

import routes
from config import Config
from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS


def create_app(config_name):
    """Creates the application and returns it to the user."""
    _app = Flask(__name__)

    _app.config.from_object(config_name)

    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            _app.register_blueprint(blueprint, url_prefix=Config.APPLICATION_ROOT)
    return _app


if __name__ == "__main__":
    app = create_app(Config)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
