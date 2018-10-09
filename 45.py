# Exercise No.45

# Create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt.
# Each file should contain a letter reflecting its filename. So, a.txt will contain
# letter a, b.txt will contain letter b and so on.


# Solution
import string

alphabet = string.ascii_lowercase
for i in alphabet:
	f_file = i + "file"
	with open("45" + i + ".txt", "w") as f_file:
		print(i, file=f_file)



