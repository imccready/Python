from flask_restful import Resource
from model.item import Item
from typing import List
from datastore import Datastore


class ItemsService(Resource):
    def get(self):
        items: List[Item] = Datastore.query(Item)
        return items

    #items: List[Item] = Datastore.query(Item)
    #return render_template("stores/stores.html", items=items)


