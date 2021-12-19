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
        return db[self.__db].find({"name": {"$regex": self.__query}})

class SearchviaAttributes():
    def __init__(self, db, marca, min, max, socket, watt):
        self.__db = db
        self.__marca = marca
        self.__min = min
        self.__max = max
        self.__socket = socket
        self.__watt = watt

    def findqueryattr(self):
        return db[self.__db].find({"marca": self.__marca, "COSTO": {"$lte" : self.__min, "$gte" : self.__max }, "socket" : self.__socket, "watt" : self.__watt})
