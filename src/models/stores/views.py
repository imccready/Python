from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from src.models.stores.store import Store

store_blueprint = Blueprint('stores', __name__)

#@store_blueprint.route('/specials/<string:name>')
@store_blueprint.route('/specials')
def show_specials(name="Woolworths"):
    items = Store.get_specials(name)
    return render_template("stores/stores.html", items=items)


#@store_blueprint.route('/scrape-specials/<string:name>')
@store_blueprint.route('/scrape-specials')
def scrap_specials(name="Woolworths"):
    url = "https://www.woolworths.com.au/shop/browse/specials/half-price"
    store = Store(name, url)
    store.store_item_specials()
    return redirect(url_for(".show_specials"))
