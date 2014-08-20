#!/usr/bin/env python


# Now that you understand that functions can be passed around as arguments
# (just like any other object), you're ready for the next step.


# First step.
# In the space below, create a function called `log_fruit`. This function
# should take an argument of `some_func`.
# On the first line of the function, place this code:
# `print "Hey, I am going to run this function ", some_func`
# And, on the second line, call the function `some_func` (like we did in the
# previous exercise)

def log_fruit(some_func):
    print "Hey, I am going to run this function ", some_func
    some_func()


# Second step
# In the space below,
# Define a function `apples`.
# On the first line of this function, use this line:
# `print "I like apples"`

def apples():
    print "I like apples"



# Third step
# In the space below, call the function `log_fruit` and pass in `apples` as an
# argument to the `log_fruit` function.
# Run this program and review the results

log_fruit(apples)



# Final step
# In the space below, write a function called `pears`.
# In the first line of the function write this code:
# `print "I am a pear"`
# DIRECTLY ABOVE (the line before your `def pears():`
# type this:
# `@log_fruit`
# Run the program and review the results

@log_fruit
def pears():
    print "I am a pear"


# Answer these two questions:
# 1) How are these two examples that are printed (apples and pears) the same
#    (if at all)? 
# 2) How are these two examples that are printed (apples and
#    pears) different (if at all)?
