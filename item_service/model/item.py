import datetime
from barely_json import parse

class Item(object):
    collection = "ItemsOnSpecial"

    def __init__(self, Barcode, Brand,  CategoryLevel1: str, CategoryLevel2: str, CategoryLevel3, SpecialsCategory, Images, ItemDetails, LastRun, Name, Price, Stockcode, Store, UnitPricing):
        self.barcode: str = Barcode
        self.brand = Brand,
        self.categoryLevel1 = CategoryLevel1,
        self.categoryLevel2 = CategoryLevel2,
        self.categoryLevel3 = CategoryLevel3,
        self.specialsCategory = SpecialsCategory,
        self.itemDetails = ItemDetails
        self.lastRun = LastRun
        self.name = Name
        self.price = Price
        self.stockcode: str = Stockcode
        self.store = Store
        self.unitPricing = UnitPricing
        self.images = Images
