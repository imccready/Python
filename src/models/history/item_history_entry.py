from src.common.date import Date


class ItemHistoryEntry(object):
    def __init__(self, store, price, date=None):
        self.store = store
        self.price = price
        self.date = date if date is not None else Date.get_today()
        #self.month = month if month is not None else Date.get_month()

    def toJSON(self):
        return {
            'store' : self.store,
            'price' : self.price,
            'date' : self.date
        }


class ItemHistoryEntryByMonth(object):
    def __init__(self, store, price, month=None):
        self.store = store
        self.price = price
        #self.date = date if date is not None else Date.get_today()
        self.month = month if month is not None else Date.get_month()

    def toJSON(self):
        return {
            'store' : self.store,
            'price' : self.price,
            'month' : self.month
        }