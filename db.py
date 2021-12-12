from flask_pymongo import MongoClient
import certifi
import os

client = MongoClient(os.environ.get("MONGODB"),tlsCAFile=certifi.where())

db = client["PAPC"]


class SearchIntoDb():
    def __init__(self, db, query):
        self.__db = db
        self.__query = query

    def findquery(self):
        return db[self.__db].find({"name": self.__query})
