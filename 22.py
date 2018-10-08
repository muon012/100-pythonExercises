# Exercise No.22

# Create a dictionary with keys a, b, c and lists 1-10, 11-20, 21-30 respectively



# Solution
import pprint # This module lets you print certain datatypes in a more readable way

pprint.pprint(dict(a=list(range(1, 11)), b=list(range(10, 21)), c=list(range(20, 31))))

