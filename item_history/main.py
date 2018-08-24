from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.api.itemhistory import itemHistory
from src.datastore import Datastore

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.before_first_request
def init_db():
    Datastore.initialize()

app.register_blueprint(itemHistory)