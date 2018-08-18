import jsonpickle
from flask import Flask, Blueprint
from flask_restful import Api, Resource
from google.cloud import pubsub_v1
import logging

from src import constants
from src.requesthelpers import RequestHelper
from src.woolworths import Woolworths

app = Flask(__name__)
api_specials_categories = Blueprint('specials-categories', __name__)
api = Api(api_specials_categories)

class SpecialsCategoriesService(Resource):

    def get(self):

        logging.error("This is error logging")
        logging.debug("This is debug logging")
        logging.info("This is info logging")
        logging.warning("This is warning logging")
        print("this is print")

        woolworths = Woolworths()
        categories = woolworths.get_categories_with_specials()
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path("python-1531294257716", "specials_categories")
        for category in categories[0:2]:

            data = {'store': constants.WOOLWORTHS,
             'data': category.json()}
            json_response = RequestHelper.post_json(constants.WOOLWORTH_ITEM_URL, category.json())
            data = u'{}'.format(data)
            logging.error("Publishing: " + data)
            publisher.publish(topic_path, data=data.encode('utf-8'))

        return {'success': 'true'}, 200




    #

api.add_resource(SpecialsCategoriesService, '/categories')