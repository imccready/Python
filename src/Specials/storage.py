from src.common.datastore import Datastore
from src.common.utilities import Utilities
from src.models.history.item_history import ItemHistory
from src.models.item import Item

from typing import List

class Storage(object):
    batch_size = 20

    @classmethod
    def store_items(cls, items):
        paged_items = Utilities.page_array(items, cls.batch_size)
        items: List(Item)
        for items in paged_items:
            item_entities_to_store = []
            item_history_entities_to_store = []

            item: Item
            for item in items:
                item_entities_to_store.append( item.get_update_entity() )

                itemHistory: ItemHistory = ItemHistory.item_to_history(item)

                item_history_entities_to_store.append( itemHistory.get_update_entity )

            Datastore.bulk_upsert( item_entities_to_store )

            Datastore.bulk_upsert(item_history_entities_to_store)


            # save items











