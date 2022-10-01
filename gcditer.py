def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == b:
        return a
    elif a > b :
        i = b
        while i <= a and i >= 2:
            if a % i == 0 and b % i == 0:
                return i
                break
            else:
                i -= 1
        return 1
    else:
        i = a
        while i <= b and i >= 2:
            if b % i == 0 and a % i == 0:
                return i
            else:
                i -= 1
        return 1