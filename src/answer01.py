#!/usr/bin/env python

# Use the sample code in example_01.py. Create three functions named
# func1, func2, and func3.
# 
# Make func1 print:
# "Hello World"
#
# Make func2 print:
# "It's nice to meet you"
#
# Make func3 print:
# "Howdeeeee"
# Put your code here:
def func1():
    print "Hello World"
var1 = func1

def func2():
    print "It's nice to meet you"
var2 = func2

def func3():
    print "Howdeeeee"
var3 = func3

def using_functions(x, y, z):
    x()
    y()
    z()

using_functions(var1, var2, var3)

# Now, make a new function called `using_functions`.
# Make it take three arguments (name the arguments as you see fit)
# Then, execute each of the arguments that you received.
# For example, if I used arguments 'a', 'b', 'c' (don't use those in
# your answer), my code would look like this:
# 
# def using_functions(a, b, c):
#   a()
#
# You are left with the exercise of calling all three functions.
