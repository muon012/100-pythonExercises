# Exercise No.69

# Please create an empty file (manually as you normally create Python files) and name it requests.py .
# Make sure the file has that name exactly.

# # This code creates the file:
# with open("requests.py", "w") as file:
# 	pass

import requests

r = requests.get("http://www.pythonhow.com")
go = requests.get("https://www.google.com")
print(r.text[:100])
print(go)

# Why does it throw an error?

# Solution
# import statements first look for a local file in the current directory (e.g. requests.py).
# If there is such file it imports that file, and not the actual module. That's why of the error.
# The solution is to named the filed another name



