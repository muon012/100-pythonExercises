# Exercise No.41

# Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.


# Solution
import string

alphabet = string.ascii_lowercase


def alphabet_file(f, list):
	with open(f, "w") as file:
		for letter in list:
			print(letter, file=file)


alphabet_file("41.txt", alphabet)



