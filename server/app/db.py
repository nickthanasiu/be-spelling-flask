from pymongo import MongoClient
from app.config import env

db_name = env['MONGODB_DATABASE']

def connect_to_db(uri):
    client = MongoClient(uri)
    return client.get_database(db_name)