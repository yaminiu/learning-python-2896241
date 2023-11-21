# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
from time import sleep


myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
mystr = "Emotional Damage"
print(mystr)

# to access a member of a sequence type, use []

print(mylist[2])
print(mytuple[1])
# use slices to get parts of a sequence

print(mylist[2:])
print(mytuple[1:3:2])
# you can use slices to reverse a sequence
print(mylist[::-1])

# dictionaries are accessed via keys


# ERROR: variables of different types cannot be combined
print(mystr, str(123))

# Global vs. local variables in functions
def someFunction():
    global mystr
    mystr = "I will send you to Jesus"
someFunction()
print(mystr, mybool, mylist, mytuple, myfloat, mydict, myint)

del mystr
del mybool
del mydict
del myfloat
del myint
del mylist
del mytuple


print("Haha, you got scammed!")
print(mystr, mybool, mylist, mytuple, myfloat, mydict, myint)


