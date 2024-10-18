import json

course = []
name = []

with open('sample.json', 'r') as json_file:
    x = json.load(json_file)

    for courses in x['certifications']:
        print(courses['courses'])

    for names in x['certifications']:
        print(names['name'])

        

