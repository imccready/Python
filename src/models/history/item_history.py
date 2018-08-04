import json

from src.common.datastore import Datastore
from src.common.utilities import Utilities
from src.models.history.item_history_entry import ItemHistoryEntry, ItemHistoryEntryByMonth


class ItemHistory(object):
    datastore_name = "ItemSpecialsHistory"

    def __init__(self, id:int, barcode:str, name:str, item_history_list_json: str=None, item_history_by_month_json: str=None):
        self.id  = id
        self.barcode = barcode
        self.name = name
        self.item_history_list = Utilities.decodeList(item_history_list_json)
        self.item_history_by_month = Utilities.decodeList(item_history_by_month_json)


    def update(self, store, price):
        # todo fix this
        item_history: ItemHistoryEntry = ItemHistoryEntry( store=store, price=price )
        if item_history not in self.item_history_list:
            self.item_history_list.append( item_history )

        item_history_by_month: ItemHistoryEntryByMonth = ItemHistoryEntryByMonth(store=store, price=price)
        if item_history_by_month not in self.item_history_by_month:
            self.item_history_by_month.append(item_history_by_month)

    def json(self) -> str:
        return {
             'id' : self.id,
             'barcode' : self.barcode,
             'name' : self.name,
             'item_history_list_json' : Utilities.encode(self.item_history_list),
             'item_history_by_month_json' : Utilities.encode(self.item_history_by_month)
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