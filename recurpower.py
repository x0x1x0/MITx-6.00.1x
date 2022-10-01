def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
temp = 1
if exp == 0:
    return temp
else:
    return base * recurPower(base,exp - 1)