#!/usr/bin/python3 -i

print("Examples for using literals in a program")

# DEFINITION CONSTANTS
LITERAL = "Literals are specific values of particular data type"
NUMBERLIT = """Numeric literals are specific numbers, whether integer or floating
point. EX: 1, -4, 3.14, 8.0"""
STRINGLIT = """String literals are enclosed in single ' or double quotes ". When
Python encounters an opening ' or ", all of the following characters up to the
closing ' or " are part of the string literal."""
LISTLIT = """List literals are enclosed in [ ] brackets. The list is composed
of a defined sequence of individual elements. Each element is accessed through
an index number from 0 to len(listlit) - 1. Different elements can be instances
of different types. EX:
    listlit = [1, False, "Hello", 3.14]
    listlit[0] == 1         # Index 0 points to the 1st element of listlit
    listlit[2] == "Hello"   # Index 2 points to the 3rd element"""
CONSTANT =  """Constant variables are meant to be set to a specific value and
then to never change throughout the execution of the program. DO NOT reassign a
constant. The names of constants are typically written in all UPPERCASE.
Constants act as placeholders for the same value in different parts of the
program. By changing a constant between program executions, the programmer can
alter the behavior of the program for different literal values."""


# Literal Examples and Types

print(0, True, "My string", 9.99)   # int, bool, str, float
print([1, 3, 5, False])             # List literal

print(3**2 + 4**2)      # Mathematical Expression with literals
print("Concatenation" + "is" + "fun")  # String concatenation with literals

print(type(1))
print(type("This string"))
print(type(True))

# Literal Assignment

i = 10
f = 4.95
b = True
s = "True"
e = ""

# Constant assignment

STR1 = "Upper case variables are constants. They keep the same literal value." 
STR2 = "Don't reassign this variable. Keep it a constant value."
PI = 3.141592653589793
SQUARED = 2

print(STR1 + STR2)  # String concatenation with constants
print(STR2 * 10)    # String multiplication with constant and literal
print(PI * 2 ** SQUARED)    # Area of a circle with literal radius of 2
print(PI * 10 ** SQUARED)   # Area of a circle with literal radius of 10


# Literals in expressions

b = 4 + 5       # Mathematical expressions
twoEven = 2 % 2 == 0    # Mixed mathematical and relational expressions
threeEven = 3 % 2 != 0
twoOdd = bool(2 % 2)    # Mixed mathematical and logical expressions
threeOdd = bool(3 % 2)

if True and True:   # Literals used in "if" condition expression
    print("Boolean literals True and False can be used in conditionals")

for i in ["This", "list", "literal", "rules"]:  # For loop over list literal
    print(i * 3)


# Literal arguments in function calls

def g(x):   # Takes integer parameter x, returns result of g(x) = x^2 + 4x + 4
    return x ** SQUARED + 4 * x + 4

print("g of 5 equals: g(5) = " + str(g(5)) )
print("g of -2 equals: g(-2) = " + str(g(-2)) )
print("g of π equals: g(PI) = " + str(g(PI)) )

y = [g(0), g(1), g(2), g(3), g(4)]  # List literal built from function calls

sum = 0
for i in range(5):
    print("g( " + str(i) + ") = " + str(y[i]) )
    sum += y[i]

print("Average = " + str(sum/5) )
