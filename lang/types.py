#!/usr/bin/python3 -i

print("Examples of data types, operations on them, and conversions")

#DEFINITIONS
TYPE = """Types determine what kind of data an object holds, and what
operations can be done on the type"""
CONSTRUCTOR = """Constructor functions return a new object of the type of the
function name. EX: i = int("15"), f = float("-5"), s = str(12)"""
INTEGER = """Integers are positive and negative whole numbers including zero.
In Python there is no limit to the size of an integer. Constructor is int()"""
FLOATING = """Floating point types represent rational numbers (decimals).
Floats have limited precision. Constructor is float()"""
BOOLEAN = """Booleans have the values True and False. Other data types can be
converted into a boolean value based on simple rules. The values 0, "", and []
are considered False as booleans, any other value is considered true. bool()"""
STRING = """String types are a sequence of text characters, useful for input
and output with the user. Text files can be stored as strings within a program.
Strings are also a sequence type and can be indexed and iterated over"""
LIST = """Lists are ordered sequences of heterogenous objects. Each individual
object of a list is called an element. Each element has its own type and can be
accessed through a numeric index. Lists are able to be iterated over. list()"""
FUNCTION = """Functions are callable objects. A function can take zero or more
input parameters and returns a single result object. Each input parameter and
the return value have their own individual types. When calling a function, the
input arguments should match the assumed type in the function definition. When
using the return value of a function call, be aware of the type. def fun():"""

# Data type from literal
print(1, type(1))
print(1.0, type(1.0))
print("1", type("1"))
print(True, type(True))
print("The print function has type " + str(type(print)) )

i = 1
f = 1.0
s = "1"
b = True
l1 = [-2, 1, 0, 1, 2]
l2 = [i, f, s, b]

def func(name):
    print("Input argument " + str(name) + " has type " + str(type(name)) )
    if type(name) == type(s):
        return "String type"
    elif type(name) == type(i):
        return "Integer type"
    elif type(name) == type(f):
        return "Float type"
    elif type(name) == type(b):
        return "Bool type"
    elif type(name) == type(l1):
        return "List type"
    else:
        return str(type(name)) + " type"
