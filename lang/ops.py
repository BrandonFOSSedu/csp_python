#!/usr/bin/python3 -i

print("Examples of different operator usage")

# DEFINITIONS
OPERATOR = """Operators take parameters and perform transformations or evaluate
functions producing a result value"""
EXPRESSIONS = """Expressions are combinations of operators and values being
operated on. Values may be literals or come from variables. Expressions are
evaluated to a final result, which is substituted in place of the original
expression"""
EVALUATION = """Evaluation is the step by step process of performing each
operation in an expression. The order of operations is determined by the
relative precedences of the operators. The result of evaluation is a final
value"""
PRECEDENCE = """Precendence is the order in which operators will be applied to
their terms. Intermediate results from prior operations are used as values in
later operations. EX:
    () func() []                Parenthesis, function calls, subscripts
    **, * / // %, + -    Mathematical
    == != < <= > >=      Relational
    not, and, or         Logical"""
COERCION = """Coercion happens when an operator is applied to different types
of values. Python will automatically coerce types into a more general type in
order to perform the operation. EX: 2 + 3.5 = 5.5 (float), True + 1 = 2.
Logical operators will automatically coerce other types to either False (zero
or empty) or True (anything else)"""

print(2 + 5*3)      # Normal PEMDAS rules
print(5 % 2 == 1)   # Relational happens last, result is a bool
print(1 and True)   # 1 is coerced to a bool (True), then "and" is evaluated

def f(x):           # Function f takes one input parameter, x
    return 2*x - 5  # f outputs result of the expression next to "return"

print(f(3) - f(2))  # Function calls evaluate first, results used for subtract

vals = [3, 4, 8, 9, 10]

print(vals[0] + vals[1]*2)  # Elements 0 and 1 from vals used in expression

def avg(numList):   # Function avg takes one input parameter, numList
    sum = 0
    for val in numList:  # Iterate through elements of list
        sum += val
    return sum / len(numList)

print(avg([5, 5, 5, 6])) # Evaluate function using list literal as argument
print(avg(vals))         # Evaluate function using variable as argument
