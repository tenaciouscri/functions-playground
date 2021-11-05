#! /usr/bin/env python3

# ----------------------------------------------------
# BASICS

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

# ----------------------------------------------------
# *ARGS AND **KWARGS

def myfunc(a,b):
    '''
    Returns 5% of the sum of a and b
    '''
    # sum() works on iterable objects like lists and
    # tuples, hence the double parenthesis
    return sum((a,b)) * 0.05

# Positional arguments: since 40 is in the first
# position, it's automatically assigned to a, the
# first argument.
print(myfunc(40,60))

# *args = arbitrary num of arguments.
def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(40,60,100,1,34))

# We use args as convention but, in general, is *
# that sets the indefinite amount of arguments.
# If we wanted to, args could be changed to anything,
# as long as it's followed by *.
def myfunc(*customname):
    return sum(customname) * 0.05

print(myfunc(40,60,100,1,34))

# *args automatically creates a tuple
# *args return a tuple
def myfunc(*args):
    for item in args:
        print(item)

# **kwargs creates a dictionary of key-valued pairs
# **kwargs return a dictionary
def myfunc(**kwargs):
    # Let's check what's in kwargs
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I didn't find any fruit here.")

myfunc(fruit = "apple", veggie = "lettuce")

# Combining *args and **kwargs
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0],kwargs["food"]))

# IMPORTANT: because we said *args first and then
# **kwargs, we must provide a list of tuples fist,
# and then dictionary elements.
myfunc(10, 20, 30, fruit = "oranges", food = "eggs", animal = "dogs")

# TASK 8: Define a function called myfunc that takes
# in an arbitrary number of arguments, and returns
# the sum of those arguments.

def myfunc(*args):
    return sum((args))

print(myfunc(10,20,30,40,50))

# TASK 9: Define a function called myfunc that
# takes in an arbitrary number of arguments and
# returns a list containing only those arguments
# that are even.

def myfunc(*args):
    mylist = []
    for item in args:
        if item % 2 == 0:
            mylist.append(item)
    return mylist

print(myfunc(1,2,3,4,5,6,11))

# TASK 10: Define a function called myfunc that
# takes in a string and returns a matching string
# where every even letter is uppercase and every
# odd letter is lowercase.

def myfunc(my_string):
    my_list = []
    for letter in range(len(my_string)):
        if letter % 2 == 0:
            my_list.append(my_string[letter].lower())
        else:
            my_list.append(my_string[letter].upper())
    return "".join(my_list)

print(myfunc("This is the beginning of the rest of your life."))

# ----------------------------------------------------

