import json

from src.common.datastore import Datastore
from src.models.history.item_history_entry import ItemHistoryEntry


class ItemHistory(object):
    datastore_name = "ItemSpecialsHistory"

    def __init__(self, id, barcode, name, item_history_list=None, item_history_by_month=None):
        self.id = id
        self.barcode = barcode
        self.name = name
        self.item_history_list = item_history_list if item_history_list is not None else []
        self.item_history_by_month = item_history_by_month if item_history_by_month is not None else []


    def update(self, store, price):
        item_history = ItemHistoryEntry( store=store, price=price )
        if item_history not in self.item_history_list:
            self.item_history_list.append( item_history )


    def json(self):
        return {
            'id' : self.id,
            'barcode' : self.barcode,
            'name' : self.name,
            'item_history_list' : "{" + json.dumps([ ob.__dict__ for ob in self.item_history_list ]) +"}",
            'item_history_by_month' : json.dumps([ ob.__dict__ for ob in self.item_history_by_month ])
        }

    @property
    def get_update_entity(self):
        return Datastore.get_entity_for_update(ItemHistory.datastore_name, self.id, self.json())

    @classmethod
    def item_to_history(cls, item):
        id = item.barcode
        print("get: {}".format(id))
        # first check if it already exists
        entity = Datastore.find_item(cls.datastore_name, id)
        if entity != None:
            item_history = ItemHistory(**entity)
            print("found")
        else:
            item_history = ItemHistory(id=id,
                                   barcode=item.barcode,
                                   name=item.name)
            print("not found")

        item_history.update(item.store, item.price)
        return item_history

    def __eq__(self, other):
        return self.id == other.id