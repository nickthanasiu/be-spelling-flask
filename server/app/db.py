from pymongo import MongoClient

def connect_to_db(uri):
    client = MongoClient(uri)
    return client.get_database('test')