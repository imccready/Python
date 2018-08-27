import jsonpickle
from flask import Flask, Blueprint
from flask_restful import Api, Resource
from google.cloud import pubsub_v1
import datetime
from logger import GoogleLogger
from src import constants
from src.requesthelpers import RequestHelper
from src.woolworths import Woolworths

app = Flask(__name__)
api_specials_categories = Blueprint('specials-categories', __name__)
api = Api(api_specials_categories)

class SpecialsCategoriesService(Resource):
    log = GoogleLogger()
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("python-1531294257716", "specials_categories")

    def get(self):
        self.log.log_text("Get specials categories")
        woolworths = Woolworths()
        categories = woolworths.get_categories_with_specials()
        lastRun = datetime.datetime.now().strftime('%d/%m/%Y')
        #for category in categories[0:1]:
        for category in categories:
            data = {
                'Store': constants.WOOLWORTHS,
                'Data': category.json(),
                'LastRun' : lastRun,
                'Description': category.description
            }
            data = u'{}'.format(data)
            self.log.log_text("Publish specials categories: " + str(data))
            self.publisher.publish(self.topic_path, data=data.encode('utf-8'))

        return 'Categories publish completed', 200

api.add_resource(SpecialsCategoriesService, '/categories')