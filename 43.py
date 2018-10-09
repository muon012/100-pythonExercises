# Exercise No.43

# Create a script that generates a file where all letters of English alphabet are listed two in each line.
# The inside of the text file would look like:
# ab
# cd
# ef


# Solution
import string

alphabet = string.ascii_lowercase


def two_letter_alphabet(f, l):
	with open(f, "w") as file:
		even = l[::2]
		odd = l[1::2]
		for j, k in zip(even, odd):
			print(j + k, file=file)


two_letter_alphabet("43.txt", alphabet)
