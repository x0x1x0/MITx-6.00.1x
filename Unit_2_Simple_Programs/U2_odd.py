"""
Write a Python function, odd, that takes in one number
and returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean
"""
# a % b gives the remainder when a is divided by b
# != checks wether its not equal to following
# if a number is odd the remainder after dividing by 2 must be
# greater than 0 - != 0

def odd(x):
    """
    x: int
    returns boolean
    """
    while x % 2 != 0:
        return True   
    return False