print("Part1: ")
dict1 = {
    "a":1,
    "b":2,
    "c":3,
}
dict2 = {
    "b":10,
    "d":4,
}
def mergeddictionaries(dict1,dict2):
    mergedict = dict1.copy()
    mergedict.update(dict2)
    return(mergedict)
mergedresults = mergeddictionaries(dict1,dict2)