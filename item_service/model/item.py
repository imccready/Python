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



    # def __init__(self, product_code, barcode, store, name, price, product_url,
    #              image_url, category, sub_category, url, last_updated=None):
    #     self.id = "{}--{}".format(store, barcode)
    #     self.barcode = barcode
    #     self.product_code = product_code
    #     self.name = name
    #     self.price = price
    #     #self.product_url = product_url
    #     self.image_url = image_url
    #     self.store = store
    #     self.category = category
    #     self.sub_category = sub_category
    #     self.url = url
        #self.last_updated = datetime.datetime.today().strftime('%d/%m/%Y') if last_updated is None else last_updated
        #self.last_updated = datetime.datetime.utcnow() if last_updated is None else last_updated
        #
        # was price
        # unit