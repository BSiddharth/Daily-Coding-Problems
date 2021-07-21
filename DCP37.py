# Easy

# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}

# using list cuz set is not indexed in python


def findPowerSet(givenList):
    length = len(givenList)
    memoryList = [[] for x in range(length+1)]
    memoryList[0].append([])

    for i in range(1, length+1):
        memoryList[i] = memoryList[i-1].copy()
        for x in memoryList[i-1]:
            y = x.copy()
            y.append(givenList[i-1])
            memoryList[i].append(y)

    print(memoryList[-1])


findPowerSet([4, 2, 9])
