from Shared.GenericMongoClient import GenericMongoClient

class MongoSingleton:
    _instance: GenericMongoClient = None

    @classmethod
    def get_singleton_client(cls, uri="mongodb://localhost:27017", db_name="test_db"):
        if cls._instance is None:
            cls._instance = GenericMongoClient(uri=uri, db_name=db_name)
            cls._instance.connect()
        return cls._instance
