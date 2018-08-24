from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from werkzeug.debug import DebuggedApplication

from api.items import api_items
from datastore import Datastore



app = Flask(__name__)
CORS(app)
api = Api(app)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.before_first_request
def init_db():
    Datastore.initialize()

app.register_blueprint(api_items)


