import pymongo
import datetime


def insertEntry():
    entryDict = {"time": datetime.datetime.now(),
                 "program": "nudes",
                 "window": "dudes"
                 }
    tracking.insert_one(entryDict)


mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = mongoClient.list_database_names()
mongoDB = 0
mongoDB = mongoClient["trackingDatabase"]

tracking = mongoDB["trackerEntry"]

insertEntry()

print(tracking.find_one())
