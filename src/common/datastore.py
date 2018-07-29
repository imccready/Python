import time

import pymongo
from google.cloud import datastore

from src import constants


class Datastore(object):
    DATASTORE_CLIENT = None

    @staticmethod
    def initialize():
        Datastore.DATASTORE_CLIENT = datastore.Client()

    @staticmethod
    def bulk_upsert(entities):
        print ("Bulk store {} entities".format( len(entities) ))
        Datastore.DATASTORE_CLIENT.put_multi(entities)

    @staticmethod
    def find_item(collection, key):
        key = Datastore.DATASTORE_CLIENT.key(collection, key)
        entity = Datastore.DATASTORE_CLIENT.get(key)
        return entity


    @staticmethod
    def get_entity(collection, key):
        entity_key = Datastore.DATASTORE_CLIENT.key(collection, key)
        entity = datastore.Entity(key=entity_key)
        return entity

    @staticmethod
    def get_entity_for_update(collection, key, data):
        entity = Datastore.get_entity(collection, key)
        entity.update(data)
        return entity


    @staticmethod
    def delete(collection):
#        db.delete(Entry.all(keys_only=True))

        key = Datastore.DATASTORE_CLIENT.key(collection)
        #Datastore.DATASTORE_CLIENT.
        #var key = ds.key(['Entry']);

        task = datastore.Entity(key=key)
        Datastore.DATASTORE_CLIENT.delete( task )

    @staticmethod
    def insert(collection, _id, data):
        task_key = Datastore.DATASTORE_CLIENT.key(collection, _id['_id'])
        task = datastore.Entity(key=task_key)
        task.update(data)
        Datastore.DATASTORE_CLIENT.put(task)


    @staticmethod
    def find(collection, query):
        #return Database.DATABASE[collection].find(query)

        dbquery = Datastore.DATASTORE_CLIENT.query(kind=collection)
        dbquery.add_filter('store', '=', query['store'])
        results = list(dbquery.fetch())
        return results

    @staticmethod
    def find_one(collection, query):
        return Datastore.DATABASE[collection].find_one(query)

    @staticmethod
    def sleep():
        # sleep to keep within google's limits
        time.sleep(constants.DATASTORE_SLEEP_TIME_SECS)
        pass
