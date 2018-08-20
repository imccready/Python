import datetime


class Item(object):
    collection = "ItemsOnSpecial"

    def __init__(self, barcode, category, image_url, last_updated, name, price, product_code, store, sub_category, url):
        self.barcode = barcode
        self.category = category
        self.image_url = image_url
        self.last_updated = last_updated
        self.name = name
        self.price = price
        self.product_code = product_code
        self.store = store
        self.sub_category = sub_category
        self.url = url
