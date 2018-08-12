from flask import Flask
from flask_restful import Api
from api.items import ItemsService
from datastore import Datastore

app = Flask(__name__)
api = Api(app)

@app.before_first_request
def init_db():
    Datastore.initialize()

api.add_resource(ItemsService, '/')




