animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

    result = 0
    big = 0
    for i in aDict.keys():
        if len(aDict[i]) >= big:
            result = i
            big = len(aDict[i])
    return result