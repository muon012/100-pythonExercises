# Exercise No.71

# Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt



# Solution
import requests

sample = requests.get("http://www.pythonhow.com/data/universe.txt")
whole_text = sample.text
a_counter = 0
for a in whole_text:
	if a == "a":
		a_counter += 1

counter_method = whole_text.count("a")
print(a_counter)
print(counter_method) # This method is preferred since it is part of the library
print(type(whole_text))

