from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from api.specialscategories import api_specials_categories
from api.specials import api_specials

app = Flask(__name__)
CORS(app)
api = Api(app)

# @app.before_first_request
# def init_db():
#     Datastore.initialize()

app.register_blueprint(api_specials_categories)
app.register_blueprint(api_specials)


