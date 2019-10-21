import pymongo
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["assign2"]
results = db["results"]
entries = db["entries"]
requestIn = db["request"]

class databaseNeeds:
    @staticmethod
    def connection(uri=""):

        client2 = pymongo.MongoClient(uri)
        if (client2 == True):
            return True
        else:
            print("server is down.")
            return False


    @staticmethod
    def printData(x):
        try:

            for document in entries.find({}, x):
                if(len(document) == 0):
                    continue
                else:
                    print(document)  # iterate the cursor
            return 10
        except :
            return 20

    @staticmethod
    def insertEntries(post_data):
        if(post_data == {}):
            return False

        entry = entries.insert_one(post_data)
        print('One post: {0}'.format(entry.inserted_id))
        return True

    @staticmethod
    def insertResults(post_data):
        if (post_data == {}):
            return False

        result = results.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))
        return True

    @staticmethod
    def insertRequest(x):
        req = requestIn.insert_one({'url':x})
        print('One post: {0}'.format(req.inserted_id))
        return True
