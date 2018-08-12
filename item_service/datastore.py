from google.cloud import datastore
from typing import TypeVar, List, Type

T = TypeVar('T')

class Datastore(object):
    DATASTORE_CLIENT: datastore.Client = None

    @staticmethod
    def initialize():
        Datastore.DATASTORE_CLIENT = datastore.Client()


    @staticmethod
    def query(cls: object) -> object:
        _query = Datastore.DATASTORE_CLIENT.query(kind=cls.collection)
        query_results =  list(_query.fetch(limit=5))
        results: List[type] = []
        for data in query_results:
            value = cls(**data)
            results.append(value)
        return results



    # for data in items_data:
    #     item = Item(**data)
    #     items.append(item)
    # return items


    @staticmethod
    def find_item(collection, key):
        key = Datastore.DATASTORE_CLIENT.key(collection, key)
        entity = Datastore.DATASTORE_CLIENT.get(key)
        return entity