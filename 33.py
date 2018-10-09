# Exercise No.33

# What will the following output?
c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())


# Solution
# 2 because calling the function foo has its own local variable that is return. The variable c inside foo is different
# than the global variable c outside the function (main program)


