# Exercise No.70

# Print out the text of this file http://www.pythonhow.com/data/universe.txt.
# Please don't manually download the file. Let Python do all the work.



# Solution
import requests

words = requests.get("http://www.pythonhow.com/data/universe.txt")
print(words.text)


