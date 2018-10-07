# Creating and appending a bunch of files with some comments in them

for i in range(9, 101):
	a = "# Exercise No." + str(i)
	b = "\n#\n\n\n\n# Solution\n\n\n"
	variable = str(i) + "_file"
	with open(str(i) + ".py", "a") as variable:
		print(b, file=variable)
