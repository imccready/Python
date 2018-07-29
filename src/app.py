from flask import Flask, render_template

from src.Specials import Specials
from src.common.datastore import Datastore

app = Flask(__name__)
app.config.from_object('config')

@app.before_first_request
def init_db():
    Datastore.initialize()


@app.route('/')
def home():
    return render_template('home.html')

from src.models.stores.views import store_blueprint
app.register_blueprint(store_blueprint, url_prefix="/stores")


if __name__ == '__main__':
    Specials.save_current_specials()

    #Database.initialize()




