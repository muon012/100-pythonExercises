# Exercise No.54

# Update the second employee's last name to "Smooth"
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}



# Solution
d["employees"][1]["lastName"] = "Smooth"
print(d["employees"][1]["lastName"])


