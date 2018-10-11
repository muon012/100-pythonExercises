# Exercise No.67

# Repeat the same functionality as before but now print a message when the word is not found
d = dict(weather="clima", earth="terra", rain="chuva")


# Solution
def translate(w):
	try:
		return d[w]
	except KeyError:
		return "Word not found"


word = input("Enter a word: ")
print(translate(word))

