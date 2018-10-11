# Exercise No.75

# Plot the data of the file into a graph of x and y axis.
# file: http://www.pythonhow.com/data/sampledata.txt


# Solution
import pandas
import matplotlib

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()

# This solution uses the pylab library which needs to be installed with pip install pylab .
# The solution has few lines of code and uses the integrated pandas plot method.
# Instead of scatter , you can specify other types of plots such as line , bar , etc.


