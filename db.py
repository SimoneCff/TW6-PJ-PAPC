from flask_pymongo import MongoClient
import certifi
import os

client = MongoClient(os.environ.get("MONGODB"), tlsCAFile=certifi.where())

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
        self.__min = int(min)
        self.__max = int(max)
        self.__socket = socket
        self.__watt = watt

    def findqueryattr(self):
        return db[self.__db].find({"marca": {"$regex": self.__marca}, "socket": {"$regex": self.__socket},
                                   "Watt": {"$regex": self.__watt}, "COSTO": {"$gte": self.__min, "$lte": self.__max}})

#
#
