# Exercise No.72

# Create a program that asks the user for an input that will be searched through google



# Solution
import webbrowser

search_query = input("Enter a word to be searched in google image results: ")
webbrowser.open("https://www.google.com/search?q=" + search_query + "&tbm=isch")
# webbrowser library lets you open websites

