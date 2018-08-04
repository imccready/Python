from src.common.date import Date

class ItemHistoryEntry(object):
    def __init__(self, store, price, date=None):
        self.store = store
        self.price = price
        self.date = date if date is not None else Date.get_today()

    def __eq__(self, other):
        return self.store == other.store and self.date == other.date


class ItemHistoryEntryByMonth(object):
    def __init__(self, store, price, month=None):
        self.store = store
        self.price = price
        self.month = month if month is not None else Date.get_month()

    def __eq__(self, other):
        return self.store == other.store and self.month == other.month
