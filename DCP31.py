# Easy

# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.
import math


def editDistanceHelper(s1, s2, memoryMatrix, i, j):

    if memoryMatrix[j][i] == math.inf:
        memoryMatrix[j][i] = min(1+editDistanceHelper(s1, s2, memoryMatrix, i-1, j),
                                 1+editDistanceHelper(s1, s2, memoryMatrix, i, j-1), editDistanceHelper(s1, s2, memoryMatrix, i-1, j-1) if s1[i-1] == s2[j-1] else math.inf, 1 + editDistanceHelper(s1, s2, memoryMatrix, i-1, j-1))
    return memoryMatrix[j][i]


def editDistance(s1, s2):
    memoryMatrix = [[math.inf for x in range(
        len(s1)+1)] for x in range(len(s2)+1)]
    for x in range(len(s2)+1):
        memoryMatrix[x][0] = x
    for x in range(len(s1)+1):
        memoryMatrix[0][x] = x

    # recursive method

    print(editDistanceHelper(s1, s2, memoryMatrix, len(s1), len(s2)))

    # iterative method

    # for x in range(1, len(s2)+1):
    #     for y in range(1, len(s1)+1):
    #         memoryMatrix[x][y] = min(1+memoryMatrix[x-1][y],
    #                                  1+memoryMatrix[x][y-1], memoryMatrix[x][y] if s1[y-1] == s2[x-1] else math.inf, 1 + memoryMatrix[x-1][y-1])

    # print(memoryMatrix[x][y])


editDistance('kitten', 'sitting')
editDistance('cat', 'bat')
