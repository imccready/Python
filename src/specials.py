from typing import List

from flask import Blueprint, render_template
from common.datastore import Datastore
from item_service.model.item import Item

specials_blueprint = Blueprint('specials', __name__)

@specials_blueprint.route('/specials')
def show_specials():
    items: List[Item] = Datastore.query(Item)
    return render_template("stores/stores.html", items=items)