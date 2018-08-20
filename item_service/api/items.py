from flask import Flask, Blueprint, request
from flask_restful import Resource, fields, marshal_with, Api, reqparse

import json
import base64
import datetime

from barely_json import parse

from logger import GoogleLogger
from model.item import Item
from typing import List
from datastore import Datastore
import uuid

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

class ItemListAPI(Resource):
    @marshal_with(fields)
    def get(self):
        items: List[Item] = Datastore.query(Item)
        return items

class ItemAPI(Resource):
    log = GoogleLogger()
    def post(self):
        self.log.log_text("Items Request: {}".format(request.data))
        try:
            request_json = self.get_json()
            key = int( request_json['Barcode'] )

            Datastore.insert(Item.collection, key, request_json)
            self.log.log_text("Success!")

        except Exception as e:
            self.log.log_error("Error occurred: " + str(e))

        return {'success': 'true'}, 200


    def get_json(self):

        request_json = json.loads(request.data.decode('utf-8'))
        payload = base64.b64decode(request_json['message']['data'])
        decode = payload.decode("utf-8").replace("'", '"')
        self.log.log_text("Data: " + decode)
        test = parse(decode)
        return test


api.add_resource(ItemListAPI, '/items')
api.add_resource(ItemAPI, '/_ah/push-handlers/item')

