# Exercise No.73

# Multiply the values in the url: https://www.pythonhow.com/data/sampledata.txt and export that ouput to a new file



# Solution
import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("73-timesTwo.txt", index=None)

# As you can see this can be done with pandas in four lines of code. We use read_csv to create a pandas data frame
# object which is like a table with data. Then we multiply this table by two and then export the calculated data to
# a text file in our local directory.
