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

from model.itemresponse import ItemResponse

app = Flask(__name__)
api_items = Blueprint('items', __name__)
api = Api(api_items)


image_fields = {
        'SmallImageFile': fields.String,
        'MediumImageFile' : fields.String,
        'LargeImageFile' : fields.String
    }

unit_pricing = {
        'UnitString': fields.String,
        'HasUnitPrice': fields.String
}

item_details = {
        'UrlFriendlyName': fields.String,
        'PackageSize': fields.String,
        'Description': fields.String,
        'IsNew': fields.Boolean,
        'FullDescription': fields.String,
        'Unit': fields.String,
        'WasPrice': fields.Price,
        'SmallFormatDescription': fields.String,
        'SavingsAmount': fields.Price
    }

item_fields =  {
        'name': fields.String,
        'price': fields.Price,
        'categoryLevel1': fields.String,
        'categoryLevel2': fields.String,
        'categoryLevel3': fields.String,
        'store': fields.String,
        'description': fields.String,
        'itemDetails': fields.Nested(item_details),
        'stockcode' : fields.String,
        'store': fields.String,
        'barcode' : fields.String,
        'images': fields.Nested(image_fields),
        'unitPricing': fields.Nested(unit_pricing),
        'brand': fields.String
    }

fields = {
        'items': fields.Nested(item_fields),
        'cursor': fields.String
    }

class ItemListAPI(Resource):
    @marshal_with(fields)
    def get(self):
        items: List[Item]
        items, next_cursor = Datastore.query_paging(Item)

        response:ItemResponse = ItemResponse()
        response.items = items
        response.cursor = next_cursor.decode("utf-8")
        return response

    @marshal_with(fields)
    def post(self):

        data = request.data.decode('utf-8')
        cursor = None
        if data:
            jsonRequest = json.loads(data)
            if 'cursor' in jsonRequest:
                cursor = jsonRequest['cursor']
                cursor = cursor.encode("utf-8")
        items: List[Item]
        items, next_cursor = Datastore.query_paging(Item, cursor)

        response: ItemResponse = ItemResponse()
        response.items = items
        response.cursor = next_cursor.decode("utf-8")
        return response


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

