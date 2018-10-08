# Exercise No.20

# Calculate the sum of all the values in the dictionary
d = {"a": 1, "b": 2, "c": 3}


# Solution
total = 0
for i in d.values():
	total += i
print(total)

print(sum(d.values()))
