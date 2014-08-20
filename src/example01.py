#!/usr/bin/env python


def function_01():
    print("This function, when executed, will print this line")


# Functions are objects (like any other). So, they can be assigned to
# variables like any other object. For example:

my_new_variable = function_01


# Now, if you wished to call this function using it's variable name,
# you would use the same syntax as normal (but on the variable). For
# example, the following executes function_01:

print "Does this work? Does this function get called?"
my_new_variable()
