#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
#Check that division output is correct
assert run("15 / 3").output == "5"
#Check that subtraction output is correct
assert run("15 - 10").output == "5"

###

print("All tests passed!")
