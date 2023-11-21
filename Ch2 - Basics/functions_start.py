#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def myFunction():
    print("This is my function")

# TODO: function that takes arguments
def myFunctionWithArguments(arg1, arg2):
    print(arg1, arg2)

# TODO: function that returns a value
def myFunctionThatReturnsAValue(arg3):
    return "This is my function " + arg3
# TODO: function with default value for an argument
def myFunctionWithADefaultValueForAnArgument(arg4, arg5=" with a default value for each argument"):
    function = arg4 + arg5
    return function
# TODO: function with variable number of arguments
def myFunctionWithAVariableNumberOfArguments(*args):
   function =  "This is my function with a variable number of arguments."
   for x in args:
       function = function+x 
   return function


myFunction()    
print(myFunction())
print(myFunction)

myFunctionWithArguments(arg1="This is my function", arg2="with arguments.")
print(myFunctionWithArguments(arg1="This is my function", arg2="with arguments."))
print(myFunctionThatReturnsAValue("that returns a value."))

print(myFunctionWithADefaultValueForAnArgument(str("This is my function")))
print(myFunctionWithADefaultValueForAnArgument("This is my function", "with a default value of each argument"))

print(myFunctionWithADefaultValueForAnArgument(arg4=" with a default value for each argument", arg5="This is my function"))
print(myFunctionWithAVariableNumberOfArguments("This is my function", "with a variable number of arguments"))