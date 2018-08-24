from google.cloud import datastore


class Datastore(object):
    DATASTORE_CLIENT: datastore.Client = None

    @staticmethod
    def initialize():
        Datastore.DATASTORE_CLIENT = datastore.Client()

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
    def find_item(collection, key):
        key = Datastore.DATASTORE_CLIENT.key(collection, key)
        entity = Datastore.DATASTORE_CLIENT.get(key)
        return entity