# Exercise No.25

# Print out the alphabet (one line for each letter)



# Solution

# for i in "abcdefghijklmnopqrstuvwxyz":
# 	print(i)

import string

for i in string.ascii_lowercase:
	print(i)
# string  is a built-in module and string.
# ascii_lowercase  returns a string object containing all 26 letters of English alphabet.
# Then we simply iterate through that string and print out the string items.


