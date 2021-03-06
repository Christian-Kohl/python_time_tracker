import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = mongoClient.list_database_names()
if "trackingDatabase" in dblist:
    mongoDB = mongoClient["trackingDatabase"]

tracking = mongoDB["trackerEntry"]
