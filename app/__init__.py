from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes import number_blueprint
    app.register_blueprint(number_blueprint, url_prefix='/api')

    return app