# Exercise No.58

# Add a new employee to the content of the file ("company1.json) so that it looks like in the expected output below:
# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'},
#                {'firstName': 'Albert', 'lastName': 'Bert'},],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}



# Solution
import json

new_employee = {"firstName": "Erick", "lastName": "Sung"}
with open("company1.json", "r+") as file:
	data = json.load(file)
	data["employees"].append(new_employee)
	file.seek(0)
	json.dump(data, file, sort_keys=True, indent=4)
	file.truncate()

# The mode "r+" means read and write. We then read the file named "file" and store its content in a variable
# named "data". We append that variable with the new entry we want to produce. After we read the file, python stopped
# reading at the last line, so we want to move to the first line, we use ".seek(0)" to do so.
# We then write to the file the new appended data, and we delete the old data in the file with ".truncate()"
