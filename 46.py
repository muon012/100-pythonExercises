# Exercise No.46

# Create a script that reads all the content in the files created in the previous exercise


# Solution
import string

alphabet = string.ascii_lowercase
new_list = []

for letter in alphabet:
	l_file = letter + "_file"
	with open("45" + letter + ".txt", "r") as l_file:
		for line in l_file:
			only_letter = line.rstrip("\n")
			new_list.append(only_letter)


print(new_list)