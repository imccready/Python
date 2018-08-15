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
        query_results =  list(_query.fetch(limit=100))
        results: List[type] = []
        for data in query_results:
            value = cls(**data)
            results.append(value)
        return results


    # @staticmethod
    # def query_paging(cls: object, cursor=None):
    #     _query = Datastore.DATASTORE_CLIENT.query(kind=cls.collection)
    #     query_iter =  _query.fetch(start_cursor=cursor, limit=100)
    #     page = next(query_iter.pages)
    #     items = list(page)
    #     results: List[type] = []
    #     for data in items:
    #         value = cls(**data)
    #         results.append(value)
    #     next_cursor = query_iter.next_page_token
    #     return results, next_cursor


    @staticmethod
    def find_item(collection, key):
        key = Datastore.DATASTORE_CLIENT.key(collection, key)
        entity = Datastore.DATASTORE_CLIENT.get(key)
        return entity