from src.common.datastore import Datastore
from src.common.utilities import Utilities
from src.models.history.item_history import ItemHistory
from src.models.item import Item


class Storage(object):
    batch_size = 20

    @classmethod
    def store_items(cls, items):
        paged_items = Utilities.page_array(items, cls.batch_size)
        for items in paged_items:
            item_entities_to_store = []
            item_history_entities_to_store = []

            for item in items:
                item_entities_to_store.append( item.get_update_entity() )

                # get current history
                item_history_entities_to_store.append( ItemHistory.item_to_history(item).get_update_entity )

            #Datastore.bulk_upsert( item_entities_to_store )

            Datastore.bulk_upsert(item_history_entities_to_store)


            #

            # save items
    @classmethod
    def update_history(cls, item_history_entities):
        pass











