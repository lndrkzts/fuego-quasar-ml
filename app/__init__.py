from flask import Flask

from .views import api_v1

app = Flask(__name__)

def create_app(enviroment):
    app.config.from_object(enviroment)
    app.register_blueprint(api_v1)
    
    return app
