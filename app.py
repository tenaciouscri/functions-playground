#! /usr/bin/env python3

# TASK 1: Write a function called myfunc that prints
# the string "Hello World"

def myfunc():
    print("Hello World")

myfunc()

# TASK 2: Define a function myfunc that takes in a
# name, and prints "Hello {name}"

def myfunc(name):
    print(f"Hello {name}")

myfunc("Cristina")

# TASK 3: Define a function called myfunc that
# takes in a Boolean value. If True, return
# "Hello", if False, return "Goodbye"

def myfunc(bool):
    if bool == True:
        return "Hello"
    elif bool == False:
        return "Goodbye"

print(myfunc(True))
print(myfunc(False))

# TASK 4: Define a function called myfunc that
# takes three arguments, x, y and z. If z is
# True, return x. If z is False, return y.

def myfunc(x, y, z):
    if z == True:
        return x
    else:
        return y
    
print(myfunc(10, 20, True))
print(myfunc("Hello", "Goodbye", False))

# TASK 5: Define a function called myfunc that
# takes in two arguments and returns their sum.

def myfunc(num1, num2):
    return (num1 + num2)

print(myfunc(7,5))

# TASK 6: Define a function called is_even that
# takes in one argument, and returns True if the
# passed-in value is even, False if it is not.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(25))
print(is_even(12))

# TASK 7: Define a function called is_greater
# that takes in two arguments, and returns True
# if the first value is greater than the second,
# False if it is less than or equal to the second.

def is_greater(num1, num2):
    if num1 > num2:
        return True
    elif num1 <= num2: # could be else only
        return False

print(is_greater(10,2))
print(is_greater(4,17))
print(is_greater(7,7))

