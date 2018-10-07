# Exercise No.12

# Create a list using my_range as the of total elements. The elements in the new list must be increments of 10.

my_range = range(1, 21)

# Solution
new_list = []
for i in my_range:
	i *= 10 # multiply i times 10 and then assign the result back to i
	new_list.append(i)
print(new_list)

# Using list compression
print([10 * x for x in my_range])




