# Exercise No.56

# Convert this dictionary into a json file
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}



# Solution
import json

with open('56.json', 'w') as fp:
    json.dump(d, fp, sort_keys=True, indent=4)

# indent=4  will create 4 white spaces to indent the different levels of the dictionary items and
# sort_keys=True tells Python to preserve the order of the dictionary thrown in the file.


