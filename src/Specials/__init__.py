from src.Specials.storage import Storage
from src.Specials.stores.Woolworths import Woolworths
from src.common.datastore import Datastore


class Specials(object):

    @staticmethod
    def save_current_specials():
        Datastore.initialize()
        woolies = Woolworths()
        specials = woolies.get_specials
        storage = Storage()
        storage.store_items(specials)
