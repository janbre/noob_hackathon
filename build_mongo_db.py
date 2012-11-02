import pymongo
import json
import os

connection = pymongo.Connection()
coll = connection.test_database.courses

path = 'fag/'
listing = os.listdir(path)
i = 0
for infile in listing:
    print infile
    current_file = open(path+infile, 'r').readline()
    course = json.loads(current_file)
    coll.insert(course)
    i += 1
    if i % 300 == 0:
        print '.'    


