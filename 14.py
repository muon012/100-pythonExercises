# Exercise No.14

# Remove the duplicates

a = ["1", 1, "1", 2]

# Solution

# This solution is easy but doesnt preserve order since sets don't have duplicates but also are unordered
print(list(set(a)))

# Preserving the order
b = []
for i in a:
	if i not in b:
		b.append(i)

print(b)
