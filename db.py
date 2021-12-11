from flask_pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@papc.q16vr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["PAPC"]
cpu = db["CPU"]

for x in cpu.find():
    print(x)
