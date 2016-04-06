"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read

def read_string():
    token_list = raw_input().split()
    if token_list[0] == "+":
        return add(int(token_list[1]), int(token_list[2]))
    if token_list[0] == "-":
        return subtract(int(token_list[1]), int(token_list[2]))
    if token_list[0] == "*":
        return multiply(int(token_list[1]), int(token_list[2]))
    if token_list[0] == "/":
        return divide(int(token_list[1]), int(token_list[2]))
    if token_list[0] == "square":
        return square(int(token_list[1]))
    if token_list[0] == "cube":
        return cube(int(token_list[1]))
    if token_list[0] == "pow":
        return power(float(token_list[1]), float(token_list[2]))
    if token_list[0] == "mod":
        return mod(int(token_list[1]), int(token_list[2]))

print read_string()