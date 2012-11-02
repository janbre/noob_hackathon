import json
course = open('test.json', 'r').readline()
d = json.loads(course)
print len(d)
