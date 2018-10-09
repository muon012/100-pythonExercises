# Exercise No.42

# Print out the sum of each column per line. Answers should be 5, 7, 9 in this order
a = [1, 2, 3]
b = (4, 5, 6)


# Solution
def adding_columns(s1, s2):
	length = len(s1)
	new_list = []
	for i in range(length):
		new_list.append(s1[i] + s2[i])
	return new_list


my_list = adding_columns(a, b)
for elem in my_list:
	print(elem)

print("=" * 20)

# BEST solution
for i,j in zip(a, b):
	print(i + j)