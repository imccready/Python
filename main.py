from flask import Flask, render_template
from typing import List
from item_service.model.item import Item
from common.datastore import Datastore

app = Flask(__name__)
app.config.from_object('config')

@app.before_first_request
def init_db():
    Datastore.initialize()


@app.route('/')
def home():
    return render_template('home.html')

from src.specials import specials_blueprint
app.register_blueprint(specials_blueprint, url_prefix="/specials")

if __name__ == '__main__':
    Datastore.initialize()
    results: List[Item] = Datastore.query('ItemsOnSpecial', Item)
    print(results)


    #specials: Specials = Specials()
    #specials.save_current_specials()