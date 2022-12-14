"""
Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding
to the entry with the largest number of elements in its list.
If there is more than one such entry, return any one of the matching keys.

For Example:

>>> biggest(animals)
    'd'

"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = 0
    big = 0
    for i in aDict.keys():
        if len(aDict[i]) >= big:
            result = i
            big = len(aDict[i])
    return result