# Exercise No.62

# Create a program that once executed the program prints Hello  instantly first,
# Then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.



# Solution
import time

counter = 0

while True:
	time.sleep(counter)
	print("Hello")
	counter += 1


