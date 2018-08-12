from src.common.datastore import Datastore
from src.models.item import Item


class Store(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return "<Store {}>".format(self.name)

    @staticmethod
    def get_specials(name):
        items = []
        items_data = Datastore.find('item_specials', {"store": name})
        for data in items_data:
            item = Item(**data)
            items.append(item)
        return items





# export GOOGLE_APPLICATION_CREDENTIALS="/Users/ianmccready/Dev/Python-3fa1a535bf19.json"