def add(num1, num2):
    return num1 + num2

# def add(nums):
#     print nums
#     result = 0
#     for num in nums:
#         result += num
#     return result 

def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    if num2 > 0:
        return num1 ** num2  # ** = exponent operator
    elif num2 == 0:
        return 1
    else:
        return 1/(num1 ** num2)


def mod(num1, num2):
    return num1 % num2
