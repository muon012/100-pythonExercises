# Exercise No.27

# Create a function that calculates the average acceleration. Pass the arguments 0, 10, 0, 20 for the parameters
# v1, v2, t1, t2 and expect the result of .5


# Solution

def avg_a(v1, v2, t1, t2):
	return (v2 - v1)/(t2 - t1)


print(avg_a(0, 10, 0, 20))
