# Exercise No.21

#  Filter the dictionary by removing all items with a value of greater than 1
d = {"a": 1, "b": 2, "c": 3}


# Solution

# Best solution:
# d = dict((key, value) for key, value in d.items() if value <= 1)
# print(d)

# Second solution:
# I added list in front of d.items() which makes a copy of the dictionary which is basically a list.
# So, when we delete items from the dictionary the loop is still iterating through the list copy which is not changing.
# So everything works fine.
for k, v in list(d.items()):
	if v > 1:
		del d[k]
# If you iterate through just "d.items()" then you get a runtime error. The reason for the error is that the
# iteration starts with a dictionary with three items but then during the iteration we are removing one of the items
# so the loop is compromised because the object (i.e. the dictionary) we are iterating through changed.


print(d)