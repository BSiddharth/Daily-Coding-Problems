# Hard

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

import math

# def largestSumHelper(numberlist,currentIndex):


def largestSumHelper(numberlist, prevLargest, prePrevlargest):
    for currentIndex in range(2, len(numberlist)):
        currentLargest = max(
            numberlist[currentIndex]+prePrevlargest, prevLargest)
        prePrevlargest = prevLargest
        prevLargest = currentLargest
    return(prevLargest)


def largestSum(numbersList):
    if len(numbersList) == 1:
        print(numbersList[0])
    elif len(numbersList) == 2:
        print(max(numbersList[0], numbersList[1]))
    else:
        prePrevlargest = numbersList[0]
        prevLargest = max(numbersList[0], numbersList[1])
        print(largestSumHelper(numbersList, prevLargest, prePrevlargest))


if __name__ == '__main__':
    largestSum([2, 4, 6, 2, 5])
    largestSum([5, 1, 1, 5])
