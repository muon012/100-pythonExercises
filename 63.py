# Exercise No.63

# Create a program that once executed the programs prints Hello  instantly first,
# then it prints it after 1 second, then after 2, 3, and then the program prints out the
# message "End of the Loop" and stops.



# Solution
import time

counter = 0
while True:
	time.sleep(counter)
	print("Hello")
	counter += 1
	if counter > 3:
		print("End of the loop")
		break
