#!/usr/bin/python3 -i

print("Examples of function definitions, usage, and return values")

# DEFINITIONS
FUNCTION = """Functions are callable objects. A function can take zero or more
input parameters and returns a single result object. Each input parameter and
the return value have their own individual types. When calling a function, the
input arguments should match the assumed type in the function definition. When
using the return value of a function call, be aware of the type. def fun():"""
DEFINEFUNCTION = """Functions must be defined before they are used. Some
functions have alread been defined and are builtin and can be used freely. A
function definition includes a function name and the names of any input
parameters. The body of the function is idented as the code block that will be
executed when a function is called. A function may return a single value, and
function execution stops when a return statement is executed."""
CALLFUNCTION = """Function calls provide a function with specific argument
values. The arguments are substituted wherever in the function body the input
parameter appears. The code of the function is executed until a return
statement or after the last statement in the body. Return values are
substituted for the function call."""

def fun1():
    print("fun1 just prints this message!")

def fun2():
    return "fun2 returns this string"

def fun3(a):
    return a * 4

def fun4(x, y):
    return bool(x % y == 0)


