from src.Specials.storage import Storage
from src.Specials.stores.Woolworths import Woolworths
from src.common.datastore import Datastore


class Specials(object):
    pass


    def save_current_specials(self):
        Datastore.initialize()
        woolies: Woolworths = Woolworths()
        specials = woolies.get_specials
        storage: Storage = Storage()
        storage.store_items(specials)
