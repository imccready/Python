from flask import Flask, Blueprint, request
from flask_restful import Resource, fields, marshal_with, Api, reqparse
import logging

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
    'url': fields.String,
    'image_url': fields.String,
    'product_code' : fields.String,
    'store': fields.String,
    'barcode' : fields.String
}

class ItemsService(Resource):
    @marshal_with(fields)
    def get(self):
        items: List[Item] = Datastore.query(Item)
        return items

    def put(self):
        logging.info("Put items...")
        test = request.data
        logging.info("items... " + str(test))
        print("items..." + str(test))
        logging.error("items... " + str(test))
        logging.debug("Debugz")
        logging.debug("items... " + str(test))


        #parser = reqparse.RequestParser()
        #parser.add_argument('test')
        ##parser.add_argument('test', type=str, help='Rate to charge for this resource')
        #args = parser.parse_args()

        #print(args)

        return {'success': 'true', 'Hello': 'World'}

api.add_resource(ItemsService, '/')
