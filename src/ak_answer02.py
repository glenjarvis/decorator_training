#!/usr/bin/env python

def log_fruit(some_func):
    print("Hey, I am going to run this function", some_func)
    some_func()

def apples():
    print("I like apples")

log_fruit(apples)

@log_fruit
def pears():
    print("I am a pear")

# Answer these two questions:
# 1) How are these two examples that are printed (apples and pears) the same
#    (if at all)? 
They are both the result of running log_fruit

# 2) How are these two examples that are printed (apples and
#    pears) different (if at all)?

output = """
('Hey, I am going to run this function', <function apples at 0xb729a1b4>)
I like apples
('Hey, I am going to run this function', <function pears at 0xb729a3ac>)
I am a pear
"""
Answer = """
One (the first, apples) results from log_fruit running the apples function,
The second (pear) results from log_fruit running the pear function.

Question still on the table: how does this syntax contribute anything?
Would it have not been simpler to remove @log_fruit from before the
'pears' function definitiong and call log_fruit(pears) after definining
pears?
"""

