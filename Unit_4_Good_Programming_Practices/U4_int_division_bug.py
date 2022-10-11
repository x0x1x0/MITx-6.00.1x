# tasked to modify the code for integerDivision so that the following error does not occur
# def integerDivision(x, a):
#     '''
#     x: a non-negative integer argument
#     a: a positive integer argument
#     returns: integer, the integer division of x divided by a.
#     '''
#     while x >= a:
#         count += 1
#         x = x - a
#     return count
# print(integerDivision(5, 3))
# File "temp.py", line 9, in integerDivision
#     count += 1
# UnboundLocalError: local variable 'count' referenced before assignment

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument
    returns: integer, the integer division of x divided by a.
    """
    # assignment has to happen before variable is referenced as stated in Errormsg
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


# print(integerDivision(5, 3))