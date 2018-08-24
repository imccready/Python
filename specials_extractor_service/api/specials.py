from flask import Flask, Blueprint, request
from flask_restful import Api, Resource
import json
import base64
from google.cloud import pubsub_v1

from logger import GoogleLogger
from src import constants
from src.requesthelpers import RequestHelper

app = Flask(__name__)
api_specials = Blueprint('specials', __name__)
api = Api(api_specials)

class SpecialsService(Resource):
    log = GoogleLogger()
    publisher = pubsub_v1.PublisherClient()
    topic_path_add_item = publisher.topic_path("python-1531294257716", "add-item")
    topic_path_add_item_history = publisher.topic_path("python-1531294257716", "add-item-history")

    def post(self):
        self.log.log_text("Specials Request: {}".format(request.data))
        try:
            request_json = self.get_json()
            self.getItems(request_json)
        except Exception as e:
            self.log.log_error( str(e) )

        return {'success': 'true'}, 200


    def getItems(self, request_json):
        url = constants.WOOLWORTH_ITEM_URL
        data = request_json['Data']

        # this a hack for now
        data['formatObject'] = "{\"name\":\"Half Price\"}"
        items_response = RequestHelper.post_json(url, data)

        #for product in items_response['Bundles'][0:1]:
        for product in items_response['Bundles']:
            product = product['Products'][0]

            self.publish_item(product, request_json)
            self.publish_item_history(product, request_json)


    #TODO Move this elsewhere
    def publish_item_history(self, product, request_json):
        item_history = {
            'Stockcode': product['Stockcode'],
            'Barcode': product['Barcode'],
            'Price': product['Price'],
            'Name': product['Name'],
            'Store': request_json['Store'],
            'Date': request_json['LastRun']
        }
        data = u'{}'.format(item_history).encode('utf-8')
        self.log.log_text("Publish items history: " + str(data))
        self.publisher.publish(self.topic_path_add_item_history, data=data)

    # TODO Move this elsewhere
    def publish_item(self, product, request_json):
        item = {
            'Stockcode': product['Stockcode'],
            'Barcode': product['Barcode'],
            'Brand': product['Brand'],
            'Price': product['Price'],
            'Name': product['Name'],
            'Store': request_json['Store'],
            'SpecialsCategory': request_json['Description'],
            'Images': {
                'SmallImageFile': product['SmallImageFile'],
                'MediumImageFile': product['MediumImageFile'],
                'LargeImageFile': product['LargeImageFile']
            },
            'UnitPricing': {
                'UnitPrice': product['CupPrice'],
                'UnitMeasure': product['CupMeasure'],
                'UnitString': product['CupString'],
                'HasUnitPrice': product['HasCupPrice'],
            },
            'ItemDetails': {
                'IsNew': product['IsNew'],
                'Description': product['Description'],
                'SmallFormatDescription': product['SmallFormatDescription'],
                'FullDescription': product['FullDescription'],
                'PackageSize': product['PackageSize'],
                'Unit': product['Unit'],
                'SavingsAmount': product['SavingsAmount'],
                'WasPrice': product['WasPrice'],
                'UrlFriendlyName': product['UrlFriendlyName'],
            },
            'CategoryLevel1': self.escape(product['AdditionalAttributes']['piesdepartmentnamesjson']),
            'CategoryLevel2': self.escape(product['AdditionalAttributes']['piescategorynamesjson']),
            'CategoryLevel3': self.escape(product['AdditionalAttributes']['piessubcategorynamesjson']),
            'LastRun': request_json['LastRun']
        }

        data = u'{}'.format(item).encode('utf-8')
        self.log.log_text("Publish items: " + str(data))
        self.publisher.publish(self.topic_path_add_item, data=data)

    def escape(self, value: str):
        return value.replace('"', '')

    def get_json(self):
        request_json = json.loads(request.data.decode('utf-8'))
        payload = base64.b64decode(request_json['message']['data'])
        decode = payload.decode('utf-8').replace("'", '"')
        return json.loads(decode)

api.add_resource(SpecialsService, '/_ah/push-handlers/specials')

