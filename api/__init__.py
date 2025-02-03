from flask import Flask
from flask_cors import CORS

def create_app():
    """
    create flask app
    """
    app = Flask(__name__)
    CORS(app)

    from api.number import number_api

    app.register_blueprint(number_api, url_prefix='/')

    return app