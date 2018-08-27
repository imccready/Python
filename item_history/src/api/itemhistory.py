from flask import Flask, Blueprint, request
from flask_restful import Resource, fields, marshal_with, Api, reqparse
from barely_json import parse
import base64
from datetime import datetime, timedelta
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
            self.storeByMonth(request_json)
            self.storeByWeek(request_json)
            self.log.log_text("Success!")

        except Exception as e:
            self.log.log_error("Error occurred: " + str(e))

        return {'success': 'true'}, 200

    def storeByWeek(self, jsonData):
        jsonData['Date'] = self.getStringDateForWed()
        key = jsonData['Barcode'] + "-" + jsonData['Date']
        item = Datastore.find_item("ItemSpecialsHistory", key)
        if item is None:
            Datastore.insert("ItemSpecialsHistory", key, jsonData)

    def storeByMonth(self, jsonData):
        jsonData['Date'] = datetime.today().strftime('%b %y')
        key = jsonData['Barcode'] + "-" + jsonData['Date']
        item = Datastore.find_item("ItemSpecialsHistoryByMonth", key)
        if item is None:
            Datastore.insert("ItemSpecialsHistoryByMonth", key, jsonData)

    def get_json(self):
        request_json = json.loads(request.data.decode('utf-8'))
        payload = base64.b64decode(request_json['message']['data'])
        decode = payload.decode("utf-8").replace("'", '"')
        self.log.log_text("Data: " + decode)
        test = parse(decode)
        return test

    def getStringDateForWed(self):
        WEDDAYOFWEEK = 2
        dayOfWeek = datetime.today().weekday()
        if (dayOfWeek < WEDDAYOFWEEK):
            dayOfWeek = dayOfWeek + 7
        dateForWed = datetime.today() + timedelta(WEDDAYOFWEEK - dayOfWeek)
        return dateForWed.strftime('%d %b %y')


api.add_resource(AddItemHistory, '/_ah/push-handlers/item-history')