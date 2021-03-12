import pymongo
import datetime


def insertEntry(program, window):
    entryDict = {"time": datetime.datetime.now(),
                 "program": program,
                 "window": window
                 }
    tracking.insert_one(entryDict)


def insertCategory(category, item):
    categoryDict = {"program": item,
                    "category": category}
    categories.insert_one(categoryDict)


def getPreviousData():
    pd = tracking.find()
    li = []
    for x in pd:
        li += [x]
    return li


mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = mongoClient.list_database_names()
mongoDB = 0
mongoDB = mongoClient["trackingDatabase"]

tracking = mongoDB["trackerEntry"]
categories = mongoDB["processCategories"]

print(tracking.find_one())
