# Exercise No.44

# Create a script that generates a file where all letters of English alphabet are listed three in each line.
# The inside of the text file would look like:
# abc
# def
# ghi



# Solution
import string

alphabet = string.ascii_lowercase + " "

print(alphabet[::3])
print(alphabet[1::3])
print(alphabet[2::3])

def letters_by_three(f, s):
	with open(f, "w") as file:
		first_letter = s[::3]
		second_letter = s[1::3]
		third_letter = s[2::3]
		for i, j, k in zip(first_letter, second_letter, third_letter):
			print(i + j + k, file=file)


letters_by_three("44.txt", alphabet)
# This is the same as the previous exercise except we are adding one white spaces to ascii_lowercase,
# so that we get a string of 27 items as opposed to 26 that ascii_lowercase  provides.
# If we slice string.ascii_lowercase we would get two slices with a length of 9 and one slice with a length of 8.
# That means the iteration would stop at the shortest slice so letters y and z wouldn't be written in the file.
# That's why we add a white space so we get three slices each with a length of 9.
# That means we get 9 iterations and not 8 as we would get with the original string.ascii_lowercase.
# The 9th iteration would write a line with the letters y and z and a white space



