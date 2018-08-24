from flask import Flask, Blueprint, request
from flask_restful import Resource, fields, marshal_with, Api, reqparse
from barely_json import parse
import base64
import datetime
import json
from logger import GoogleLogger
from src.datastore import Datastore

app = Flask(__name__)
itemHistory = Blueprint('item-history', __name__)
api = Api(itemHistory)



class AddItemHistory(Resource):
    log = GoogleLogger()

    def post(self):
        self.log.log_text("Items Request: {}".format(request.data))

        try:
            request_json = self.get_json()
            request_json['Month'] = datetime.datetime.today().strftime('%b %y')

            key = request_json['Barcode'] + "-" + request_json['Month']

            item = Datastore.find_item("ItemSpecialsHistory", key)
            if item is None:
                Datastore.insert("ItemSpecialsHistory", key, request_json)

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


api.add_resource(AddItemHistory, '/_ah/push-handlers/item-history')