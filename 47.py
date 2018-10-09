# Exercise No.47

# Loop through the files from exercise 45 and read the contents of each one. If the file contains any letter in the
# string "python" then add it to a list and display such list


# Solution
import string

alphabet = string.ascii_lowercase
python_list = []

for letter in alphabet:
	l_file = letter + "_file"
	with open("45" + letter + ".txt", "r") as l_file:
		for line in l_file:
			only_letter = line.rstrip("\n")
			if only_letter in "python":
				python_list.append(only_letter)


print(python_list)


