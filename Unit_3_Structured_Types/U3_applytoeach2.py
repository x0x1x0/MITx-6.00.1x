"""
Here is the code for a function applyToEach:

    def applyToEach(L, f):
        for i in range(len(L)):
            L[i] = f(L[i])

Assume that: testList = [1, -4, 8, -9]
    
    >>> print(testList)
    [2, -3, 9, -8]
  
  
  """
  
def addOne(a):
    return a + 1

applyToEach(testList, addOne)