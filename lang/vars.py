#!/usr/bin/python3 -i

print("Examples of Variable assignment and usage")

# DEFINITION CONSTANTS
VARIABLE = """A variables consists of a variable name (identifier), a data
type, and a value."""
ASSIGNMENT = """Assignment statements can create or reassign variables. EX: var =
value. After an assignment, the new value will be substituted for the
variable's name where it appears in later statements."""
SUBSTITUTION = """Substitution occurs when a variable name appears in a statement
or expression after a value has been assigned to a variable. EX: var -> val"""
OBJECT = """Everything in Python is an object. Variable names "point' at
objects after assignment. Variable values during substitution depend on the
data that an object instance has available. Multiple variable names can point
at the same object. EX: a = 4, b = 4, id(a) == id(b)"""

# Assignment Statements
# Variables are created the first time a new name appears in an assignment
# Variables can be reassigned to a new value, the old value is lost
# The value of a variable is 

a = 5   # Create variable "a" and assign it the value "5"
b = 9   # Create variable "b" and assign it the value "9"
print(a, b)

c = a   # Create variable "c" and point it at same object as "a"
print(a, id(a))
print(c, id(c))

a = -5  # Reassign variable "a" to "-5". New value also means new object
print(a, id(a))
print(c, id(c))

# Variable swap
# To swap the value of two variables, a third variable is needed so that values
# are not overwritten

tmp = c
c = a
a = tmp
print(a, id(a))
print(c, id(c))


# Variable types
# The value of a variable is dependent upon the types of values that an object
# has available from it's data type

intVar = 99     # Create 4 variables assigned to objects of different types
floatVar = 3.14
strVar = "Hello, world"
boolVar = True
listVar = [intVar, floatVar, strVar, boolVar]

print(intVar, floatVar, strVar, boolVar) # Print can convert type of argument
print(type(intVar), type(floatVar), type(strVar), type(boolVar)) 
print(listVar)
print(type(listVar))

int2float = float(intVar)
float2str = str(floatVar)
str2bool = bool(strVar)
bool2int = int(boolVar)

print(int2float, type(int2float))
print(float2str, type(float2str))
print(str2bool, type(str2bool))
print(bool2int, type(bool2int))


# Variables in expressions
# When variable names are used in expressions, the value for that data type is
# substituted for the variable name. The data type of the variable determines
# how an operation is performed. Variables may appear on the expression side of
# their own assignment statement

a = b*2 - a     # a = 9*2 - 5 = 13, the "*" performs multiplication
hello3 = strVar * 3     # The "*" performs string repetition
boolLogic = boolVar and True and 1 and "Yes"  # Other types become bool

print(a, hello3, boolLogic)


# Variable assignment operators
# Variables can be reassigned from a an expression using a shorthand notation

a += 2      # a = a + 2
b *= 4      # b = b * 4
c %= 3      # c = c % 3


# Variables in functions
# Function definition may include input parameters. The names of the parameters
# are set in the function definition header. The parameter variables can appear
# anywhere in the function body. When the function is called, each occurrence
# of the parameter variable is replaced by the actual input arguments.

def myFunc (x):
    print(x)
    x += x * 3 - 5
    return x

ans1 = myFunc(4)    # Variable assignment from result of function call
ans2 = myFunc(a)
print(ans1)
print(ans2)
print(myFunc(a + b))    # Function call with variable expression argument
