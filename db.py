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
        self.__min = min
        self.__max = max
        self.__socket = socket
        self.__watt = watt

    def findqueryattr(self):
        print(self.__watt, self.__max, self.__min, self.__socket, self.__marca)
        return db[self.__db].find({"marca": {"$regex": self.__marca}, "socket": {"$regex": self.__socket},
                                   "watt": {"$regex": self.__watt}})
