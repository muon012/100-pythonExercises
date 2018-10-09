# Exercise No.34

# Fix the function so that there is no error and the last line is able to print out the value of c  (i.e. 1 ).
def foo():
    c = 1
    return c
foo()
print(c)


# Solution


def foo():
	global c
	c = 1
	return c


foo()
print(c)

# Adding 'global c'  fixes the code. That line makes available name c  in the global namespace.
# Therefore,  print is able to access variable c .


