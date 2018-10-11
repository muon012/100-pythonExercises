# Exercise No.74

# Concatenate these two files to show this output:
# 	x,y
# 	3,5
# 	4,9
# 	6,10
# 	7,11
# 	8,12
# 	6,10
# 	8,18
# 	12,20
# 	14,22
# 	16,24

# First file: http://www.pythonhow.com/data/sampledata.txt
# Second file: http://pythonhow.com/data/sampledata_x_2.txt

# Solution
import pandas

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
new_data = pandas.concat([data1, data2]) # Must pass an iterable object
new_data.to_csv("74-pandas.txt", index=None)

# We are using pandas to load the data into Python. Then we use the concat method.
# This method expects as input a list of data frame objects to be concatenated.
# Lastly, we export the data to a new text file.

