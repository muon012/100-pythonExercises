# Exercise No.10

# Complete the script so that it prints out a list slice containing letters a, c, e, g, and i.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Solution
print(letters[::2])
# The complete syntax of list slicing is [start:end:step] .
# When you don't pass a step, Python assumes the step is 1. [:]  itself means get everything from start to end.
# So, [::2]  means get everything from start to end at a step of two.
# But remember that passing an upper bound will exclude that last number.
