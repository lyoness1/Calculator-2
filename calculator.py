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


def intergerize(str_list):
    """returns a list of integers from a list of strings"""
    return map(int, str_list)


def read_string():
    token_list = raw_input().split()
    # original code: 
    # if token_list[0] == "+":
    #     return add(int(token_list[1]), int(token_list[2]))
    # code for taking multiple inputs - adjusted in arithmetic.py: 
    # if token_list[0] == "+":
    #     return add(map(int, token_list[1:]))
    if token_list[0] == "+": # code for using reduce() for multiple nums
        return reduce(add, intergerize(token_list[1:]))
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
    else:
        print "invalid operation"

# my version of reduce()
def my_reduce(func, iterable, initialzer=None):
    if initialzer is not None:
        answer = initialzer
    else:
        answer = iterable[0]
        iterable = iterable[1:]
    for i in iterable:
        answer = func(answer, i)
    return answer

print read_string()

