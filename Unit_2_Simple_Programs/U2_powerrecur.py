"""
In Problem 1, we computed an exponential by iteratively executing successive multiplications.
We can use the same idea, but in a recursive function.

Write a function recurPower(base, exp) which computes base^exp
by recursively calling itself to solve a smaller version of the same problem, 
and then multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer;
exp will be an integer >= 0  . It should return one numerical value.
Your code must be recursive - use of the ** operator or looping constructs is not allowed.
"""
# the recursive function calls upon itself.
# a good way to think about this is following.
# everytime the function calls upon itself it creates a new scope.
# in this case it stops calling itself once the exp is equal to 0.
# at that point it returns temp (1) to the last scope that called the function.
# the first returnvalue is 1
# the next returnvalue is base*1
# it then in a way "eats up" the scope next up by returning a value for it
# think of it as a function that creates new scopes every time it calls itself, without returning a value.
# once it stops recursively calling itself it conquers all its return values.
# and gives them to the before created scope that asked for it.
# it now uses these returned values to return new values until every created scope.
# has had its return value to work with.

# each recursive call to a function creates its own scope/environment
# bindings of variables in a scope is not change by recursive call
# flow of control passes back to previous scope once function call returns value

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    temp = 1
    if exp == 0:
        return temp
    else:
        return base * recurPower(base,exp - 1)   