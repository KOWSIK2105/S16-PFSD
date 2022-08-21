import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

#If you have a JSON string, you can parse it by using the json.loads() method.

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])