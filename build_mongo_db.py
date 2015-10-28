import pymongo
import json
import os

client = pymongo.MongoClient()
db = client.test_database.courses

path = 'fag/'
listing = os.listdir(path)
for infile in listing:
    print (infile)
    current_file = open(path+infile, 'r').readline()
    course = json.loads(current_file)
    db.insert_one(course)


