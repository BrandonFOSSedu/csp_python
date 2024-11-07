#!/usr/bin/python3 -i

print("Examples of data types, operations on them, and conversions")

#DEFINITIONS
TYPE = """Types determine what kind of data an object holds, and what
operations can be done on the type"""
CONSTRUCTOR = "Constructor functions return a new object of the type of the
function name. EX: i = int("15"), f = float("-5"), s = str(12)"""


# Data type from literal
print(1, type(1))
print(1.0, type(1.0))
print("1", type("1"))
print(True, type(True))

i = 1
f = 1.0
s = "1"
b = True

print(i + 2)
