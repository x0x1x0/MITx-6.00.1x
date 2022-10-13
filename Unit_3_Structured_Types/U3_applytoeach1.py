"""
Here is the code for a function applyToEach:

    def applyToEach(L, f):
        for i in range(len(L)):
            L[i] = f(L[i])

Assume that: testList = [1, -4, 8, -9]
    
    >>> print(testList)
    [1, 4, 8, 9]
  
  
  """
  
def absolute(a):
    return abs(a)

applyToEach(testList, absolute)

#or

applyToEach(testList, abs)