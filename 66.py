# Exercise No.66

# Create an English to Portuguese translation program.
# The program takes a word from the user and translates it using the following dictionary as a vocabulary source.
d = dict(weather="clima", earth="terra", rain="chuva")


# Solution
def translate(w):
	return d[w]


word = input("Enter the word 'earth'/'weather'/'rain': ")
print(translate(word))
