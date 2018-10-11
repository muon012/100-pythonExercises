# Exercise No.68

# Repeat the same functionality as before but now make the program non case-sensitive meaning that for example,
# both earth and Earth should return the translation correctly for that word.
d = dict(weather="clima", earth="terra", rain="chuva")


# Solution
def translate(w):
	low = w.lower()
	try:
		return d[low]
	except KeyError:
		return "There is no such word"


x = input("Enter a word: ")
print(translate(x))


