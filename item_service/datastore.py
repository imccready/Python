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
        query_results =  list(_query.fetch())
        results: List[type] = []
        for data in query_results:
            value = cls(**data)
            results.append(value)
        return results

    @staticmethod
    def insert(collection, key, data, excludeFromIndex=None):
        task_key = Datastore.DATASTORE_CLIENT.key(collection, key)
        if excludeFromIndex is not None:
            task = datastore.Entity(key=task_key,
                                exclude_from_indexes=excludeFromIndex)
        else:
            task = datastore.Entity(key=task_key)
        task.update(data)
        Datastore.DATASTORE_CLIENT.put(task)



    @staticmethod
    def query_paging(cls: object, cursor=None):
         _query = Datastore.DATASTORE_CLIENT.query(kind=cls.collection)
         _query.order = ['Brand']
         query_iter =  _query.fetch(start_cursor=cursor, limit=20)
         page = next(query_iter.pages)
         items = list(page)
         results: List[type] = []
         for data in items:
             value = cls(**data)
             results.append(value)
         next_cursor = query_iter.next_page_token
         return results, next_cursor


    @staticmethod
    def find_item(collection, key):
        key = Datastore.DATASTORE_CLIENT.key(collection, key)
        entity = Datastore.DATASTORE_CLIENT.get(key)
        return entity