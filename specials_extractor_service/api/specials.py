from flask import Flask, Blueprint, request
from flask_restful import Api, Resource
import logging
import json
import base64
from google.cloud import pubsub_v1

from src import constants
from src.requesthelpers import RequestHelper


app = Flask(__name__)
api_specials = Blueprint('specials', __name__)
api = Api(api_specials)


class SpecialsService(Resource):
    def post(self):
        logging.error(request.data)

        request_json = self.get_json()

        url = constants.WOOLWORTH_ITEM_URL
        data = request_json['data']

        # this a hack for now
        data['formatObject'] = "{\"name\":\"Half Price\"}"
        items_response = RequestHelper.post_json(url, data)

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path("python-1531294257716", "add-item")

        for product in items_response['Bundles'][0:10]:
            product = product['Products'][0]
            data = u'{}'.format(product).encode('utf-8')
            logging.error(data)
            publisher.publish(topic_path, data=data)

        return {'success': 'true'}, 200


    def get_json(self):
        request_json = json.loads(request.data.decode('utf-8'))
        payload = base64.b64decode(request_json['message']['data'])
        decode = payload.decode('utf-8').replace("'", '"')
        logging.error("Decode: " + decode)
        return json.loads(decode)

api.add_resource(SpecialsService, '/_ah/push-handlers/specials')

#https://specials-extractor-dot-python-1531294257716.appspot.com/_ah/push-handlers/specials

#gcloud pubsub subscriptions pull --auto-ack specials_categories
