from src.common.datastore import Datastore
from src.common.webdriver import Webdriver
from src.models.item import Item
from src.models.pages.page import Page


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


    def store_item_specials(self):
        webdriver = Webdriver(self.url)
        page = Page(self.name)

        isNext = True
        i = 1
        while i < 2 and isNext == True:
            print("Page #: {}".format(i))
            items = page.get_items(webdriver)
            isNext = page.is_next_page(webdriver)
            i = i+1

        webdriver.finish()
        print("Finished")


# export GOOGLE_APPLICATION_CREDENTIALS="/Users/ianmccready/Dev/Python-3fa1a535bf19.json"