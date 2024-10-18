import json
import yaml

#example of json

x = '{"name":"Jhon","age":"30","city":"New York City"}'

#parse json

y = json.loads(x)
print("The out of json file is ", y)
print("Name: {}\nAge: {}\nCity: {}".format(y["name"], y["age"], y["city"]))

