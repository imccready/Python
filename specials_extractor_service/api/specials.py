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
    topic_path = publisher.topic_path("python-1531294257716", "add-item")

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
        lastRun = request_json['LastRun']
        store = request_json['Store']
        specialDesc = request_json['Description']

        # this a hack for now
        data['formatObject'] = "{\"name\":\"Half Price\"}"
        items_response = RequestHelper.post_json(url, data)

        #for product in items_response['Bundles'][0:1]:
        for product in items_response['Bundles']:
            product = product['Products'][0]

            item = {
                'Stockcode': product['Stockcode'],
                'Barcode':product['Barcode'],
                'Brand': product['Brand'],
                'Price': product['Price'],
                'Name': product['Name'],
                'Store': store,
                'Description': specialDesc,
                'Images': {
                    'SmallImageFile': product['SmallImageFile'],
                    'MediumImageFile': product['MediumImageFile'],
                    'LargeImageFile': product['LargeImageFile']
                },
                'UnitPricing' : {
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
                'CategoryLevel-1': self.escape ( product['AdditionalAttributes']['piesdepartmentnamesjson'] ),
                'CategoryLevel-2': self.escape ( product['AdditionalAttributes']['piescategorynamesjson'] ),
                'CategoryLevel-3': self.escape ( product['AdditionalAttributes']['piessubcategorynamesjson'] ),
                'LastRun': lastRun
            }

            data = u'{}'.format(item).encode('utf-8')
            self.log.log_text("Publish specials: " + str(data))
            self.publisher.publish(self.topic_path, data=data)



    def escape(self, value: str):
        return value.replace('"', '')

    def get_json(self):
        request_json = json.loads(request.data.decode('utf-8'))
        payload = base64.b64decode(request_json['message']['data'])
        decode = payload.decode('utf-8').replace("'", '"')
        return json.loads(decode)

api.add_resource(SpecialsService, '/_ah/push-handlers/specials')

