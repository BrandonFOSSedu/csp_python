#!/usr/bin/python3 -i

print("Examples of random module and its functions")

# DEFINITIONS
MODULE = """Modules are collections of code that can be imported and used in
other Python programs. EX: import random. The functions available in a module
are accessed by using "dot" notation. EX: module.function()."""
RANDOM = """Random module contains functions for getting random values.
Available functions can choose a random float between 0 and 1, a random integer
between START and STOP, or a random element from a list. EX:
    0 <= random.random() < 1
    START <= random.randint(START, STOP) <= STOP
    random.choice([2, 3.14, True, "String"])"""
PROBABILITY = """Random can help simulate probabilities by controlling the
number of possible outcomes with specific ranges of outcomes. EX:
    random.choice([1, 2, 3])  1/3 probability for any element
    random.choice([1, 1, 2])  2/3 probability for 1, 1/3 probability for 2
    random.random() < .3      30% probability
    random.randint(1, 100) < 43   43% probability"""

# Random module basics

import random   # Import statement for random module

print(random.random())  # 0 <= float < 1
print(random.random())

print(random.randint(1, 10))    # 1 <= int <= 10
print(random.randint(1, 10))

vals = [1, 3, 5, 7, 9]
print(random.choice(vals))      # random element of vals list
print(random.choice(vals))


# Random for probability

for i in range(10):  # Iterate over code block 10 times
    f = random.random()
    if f >= .1 and f <= .25:    # .25-.1 = 15% probability
        print("Triaf #" + str(i) + " - " + str(f) + " - 15% probability here")
    else:
        print("Trial #" + str(i) + " - " + str(f) + " - 85% probability here")


rarity = random.randint(1, 100)

if rarity <= 10:    # 10% probability
    print("Rare")
elif rarity <= 40:  # 40% - 10% = 30% probability
    print("Uncommon")
elif rarity <= 99:  # 99% - 40% = 49% probability
    print("Common")
else:               # 100% - 99% = 1% probability
    print("Ultra Rare")


def randDrop():     # Uses probability to weight random drop, returns string
    dropProb = random.randint(1, 10)

    if dropProb > 9:    # 2/10 = 20% probability
        drop = "weapon"
    elif dropProb > 6:  # 3/10 = 30% probability
        drop = "item"
    elif dropProb == 5: # 1/10 = 10% probability
        drop = "armor"
    else:
        drop = "nothing"  # 4/10 = 40% probability

    return drop

for i in range(10):     # Iterate loop body 10 times
    print(randDrop())   # Print string result of randDrop call


