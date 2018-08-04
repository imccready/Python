import datetime
import uuid

from src.common.datastore import Datastore


class Item(object):
    item_datastore_name = "ItemsOnSpecial"

    def __init__(self, product_code, barcode, store, name, price, product_url, image_url, category, sub_category, last_updated=None):
        self.id = "{}--{}".format(store, barcode)
        self.barcode = barcode
        self.product_code = product_code
        self.name = name
        self.price = price
        self.product_url = product_url
        self.image_url = image_url
        self.store = store
        self.category = category
        self.sub_category = sub_category
        #self.last_updated = datetime.datetime.today().strftime('%d/%m/%Y') if last_updated is None else last_updated
        self.last_updated = datetime.datetime.utcnow() if last_updated is None else last_updated
        #
        # was price
        # unit

    def __repr__(self):
        return "<Item {} with Price {} and URL {}>".format(self.name, self.price, self.url)


    def get_update_entity(self):
        entity = Datastore.get_entity_for_update(Item.item_datastore_name, self.id, self.json())
        entity.exclude_from_indexes = "[image_url, url]"
        return entity

    def save_to_db(self):
        Datastore.insert(collection='item_specials',
                         _id = {"_id": self.id},
                         data=self.json())

    def json(self):
        return {
            'store': self.store,
            'name': self.name,
            'barcode': self.barcode,
            'product_code': self.product_code,
            'price': self.price,
            'url': self.product_url,
            'image_url': self.image_url,
            'category' : self.category,
            'sub_category' : self.sub_category,
            'last_updated' : self.last_updated

        }

    def is_equal(self, item):
        return self.id == item.id

            #'last_date': self.last_date



#https://www.woolworths.com.au/apis/ui/PiesCategoriesWithSpecials/

#post -> https://www.woolworths.com.au/apis/ui/browse/category
