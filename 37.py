# Exercise No.37

# Create a function that takes a text file as input and returns the number of words contained in the text file.
# Please take into consideration that some words can be separated by a comma with no space.
# For example "Hi,it's me." would need to be counted as three words.
# For your convenience, you can use the text file in the attachment.


# Solution
def count_words_file(f):
	with open(f, "r") as file:
		words = 0
		new_line = str() # Declare and initialize a variable that will hold the new line with replaced commas
		for line in file:
			new_line = line.replace(",", " ")
			words += len(new_line.split())
		return words


print(count_words_file("words2.txt"))


