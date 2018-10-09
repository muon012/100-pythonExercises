# Exercise No.28

# Why is there an error?


def foo(a, b):
	print(a + b)

x = foo(2, 3) * 10


# Solution
# Python cannot multiply a None type object with an integer.
# The function output is what produces a None object because the function definition is not returning anything.
# You can fic it by using 'return' rather than 'print' in the function definition

