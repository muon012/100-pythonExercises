# Exercise No.55

# Add a new employee
d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}

# Solution
import pprint

d["employees"].append({"firstName": "Kyle", "lastName": "Morgan"})
pprint.pprint(d["employees"])


