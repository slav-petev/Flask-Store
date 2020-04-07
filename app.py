from flask import Flask
from flask_restful import Api
from flask_injector import FlaskInjector
from injector import singleton
from dependencies import configure

from shared.interfaces.configuration import Configuration
from routes import configure_routes


app = Flask(__name__)
api = Api(app)
injector = FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
    configure_routes(api)
    config = injector.injector.get(Configuration, scope=singleton)
    app_section = config.get_app_section()
    app.run(port=app_section.port, debug=app_section.debug_mode)