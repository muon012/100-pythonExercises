# Exercise No.36

# Create a Python function that takes a text file as input and returns the number of words contained in the text file
# Use "words1.txt"


# Solution
def count_file_words(f):
	with open(str(f), "r") as fileRead:
		words_len = 0
		for line in fileRead:
			words_len = len(line.split())
		return words_len


print(count_file_words("words1.txt"))


