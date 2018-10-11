# Exercise No.59

# Complete the code so that it prints out the expected output:
# Item 1 has index 0
# Item 2 has index 1
# Item 3 has index 2

a = [1, 2, 3]


# Solution
for i in a:
	print("Item {} has index {}".format(i, a.index(i)))

for index, element in enumerate(a):
	print("Item {} has index {}".format(element, index))

# Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
# The __next__() method of the iterator returned by enumerate() returns a tuple containing a count
# (from start which defaults to 0) and the values obtained from iterating over iterable.


