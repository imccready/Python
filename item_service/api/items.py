from flask import Flask, Blueprint
from flask_restful import Resource, fields, marshal_with
from flask_restful import Api

from model.item import Item
from typing import List
from datastore import Datastore


app = Flask(__name__)
api_items = Blueprint('items', __name__)
api = Api(api_items)

fields = {
    'name': fields.String,
    'price': fields.Price,
    'category': fields.String,
    'sub_category': fields.String,
    'store': fields.String,
    'url': fields.String
}

class ItemsService(Resource):
    @marshal_with(fields)
    def get(self):
        items: List[Item] = Datastore.query(Item)
        return items

api.add_resource(ItemsService, '/')
