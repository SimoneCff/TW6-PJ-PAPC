from flask_pymongo import MongoClient, ObjectId
import certifi
import os

client = MongoClient(os.environ.get("MONGODB"), tlsCAFile=certifi.where())

db = client["PAPC"]


class searchviaid():
    def __init__(self, id, dat):
        self.__id = ObjectId(id)
        self.__dat = dat

    def findquery(self):
        return db[self.__dat].find_one({"_id": self.__id})


class SearchIntoDb():
    def __init__(self, db, query):
        self.__db = db
        self.__query = query

    def findquery(self):
        return db[self.__db].find({"name": {"$regex": self.__query}})


class SearchviaAttributesCPU():
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


class SearchviaAttributesCool():
    def __init__(self, db, marca, min, max, socket, watt, type):
        self.__db = db
        self.__marca = marca
        self.__min = int(min)
        self.__max = int(max)
        self.__type = type

    def findqueryattr(self):
        return db[self.__db].find({"marca": {"$regex": self.__marca},"COSTO": {"$gte": self.__min, "$lte": self.__max},
                                   "tipo": {"$regex": self.__type}})


class SearchviaAttributesCASE():
    def __init__(self, db, marche, min, max, model):
        self.__db = db
        self.__marche = marche
        self.__min = int(min)
        self.__max = int(max)
        self.__model = model

    def findqueryattr(self):
        return db[self.__db].find({"marca": {"$regex": self.__marche}, "model": {"$regex": self.__model},
                                   "COSTO": {"$gte": self.__min, "$lte": self.__max}})


class SearchviaAttributesMobo():
    def __init__(self, db, marca, min, max, socket, watt, model, clock):
        self.__db = db
        self.__marca = marca
        self.__min = int(min)
        self.__max = int(max)
        self.__socket = socket
        self.__watt = watt
        self.__model = model
        self.__clock = clock

    def findqueryattr(self):
        return db[self.__db].find({"marca": {"$regex": self.__marca}, "socket": {"$regex": self.__socket},
                                   "Watt": {"$regex": self.__watt}, "COSTO": {"$gte": self.__min, "$lte": self.__max},
                                   "model": {"$regex": self.__model}, "clock-r": {"$regex": self.__clock}})


class SearchviaAttributesPSU():
    def __init__(self, db, marca, min, max, watt):
        self.__db = db
        self.__marca = marca
        self.__min = int(min)
        self.__max = int(max)
        self.__watt = watt

    def findqueryattr(self):
        return db[self.__db].find({"marca": {"$regex": self.__marca}, "Watt": {"$regex": self.__watt},
                                   "COSTO": {"$gte": self.__min, "$lte": self.__max}})
