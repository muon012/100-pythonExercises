# Exercise No.24

# Print out this output:
# b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))



# Solution
for keys in sorted(d.keys()):
	print("{} has a value of {}".format(keys, d[keys]))



