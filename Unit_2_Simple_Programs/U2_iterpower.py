


"""
Write an iterative function iterPower(base, exp) that calculates the exponential base^exp by simply using successive multiplication.
For example, iterPower(base, exp) should compute base^exp by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer;
exp will be an integer >= 0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.
"""

# function takes in an int or float, aswell as exponent.
# it now just iterates over the while loop as long as the exponent is greater than 1.
# after each loop it decreases the exp by 1.
# Therefore it first multiplies temp * base exp times.
# given the two ints 4, 3 we get 1*4, 4*4, 16*4 and result in the return of temp as 64.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    temp = 1
    while exp > 0:
        temp *= base
        exp -= 1
    return temp
