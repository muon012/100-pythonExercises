# Exercise No.57

# Print out this content from the file "company1.json:
# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}



# Solution
import json
import pprint

with open("company1.json", "r") as json_file:
	data = json.load(json_file)

pprint.pprint(data)

# json.loads vs json.load
# json.loads  expects a string input containing json data "data = json.loads(json_file.read()) " ,
#  while json.load  expects a file object (not a file path).


