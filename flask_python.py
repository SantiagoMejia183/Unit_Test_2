from databaseFunc import databaseNeeds
from pymongo import MongoClient


from flask import Flask
client = MongoClient("mongodb://localhost:27017/")
db = client.assign2
results = db["results"]
entries = db["entries"]
requestIn = db["request"]


app = Flask(__name__)



@app.route("/distance/")
def distanceHTTP():
    pymongo_cursor = db.collection.find()
    allDistData = ''
    databaseNeeds.insertRequest("localhost:27017/distance")
    for document in entries.find({}, {"_id": 0, "x1": 1, "x2": 1, 'y1': 1, "y2": 1, "timestamp": 1}):
        #print(document)  # iterate the cursor
        tempRetire = str(document)
        allDistData = allDistData + tempRetire

    return allDistData

@app.route("/retirement/")
def retirementHTTP():
    pymongo_cursor = db.collection.find({})
    allRetireData = ''
    databaseNeeds.insertRequest("localhost:27017/retirement")
    for document in retireEntries.find({}, {"_id": 0, "age": 1, "annualSalary": 1, 'percentSaved': 1,
                                            "retirementSaveGoal": 1}):
        #print(document)  # iterate the cursor
        tempRetire = str(document)
        allRetireData = allRetireData + tempRetire

    return allRetireData

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
