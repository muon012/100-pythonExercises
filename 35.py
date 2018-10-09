# Exercise No.35

# Create a function that takes any string as input and returns the number of words for that string.


# Solution

def len_wrd(a):
	return len(a.split())


x = input("Write a sentence: ")
print(len_wrd(x))

# The split function splits a string by the argument you passed through it, default is space, and returns a list of
# such "split" elements
