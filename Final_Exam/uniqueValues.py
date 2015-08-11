def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    hDict = {}
    uniqueValues = []
    for key in aDict.keys():
        hDict[key] = aDict.values().count(aDict[key])
    for key in hDict.keys():
        if hDict[key] == 1:
            uniqueValues.append(key)
    return sorted(uniqueValues)
       
