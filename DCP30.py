# Medium

# This problem was asked by Facebook.

# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


def findWaterCapacity(surfaceElevationList):

    if len(surfaceElevationList) in (0, 1, 2):
        print(0)
        return
    start = 0
    end = 0
    maxHeight = 0
    minHeight = surfaceElevationList[start]
    capacity = 0
    for index in range(1, len(surfaceElevationList)):
        if surfaceElevationList[index] < surfaceElevationList[start]:
            if surfaceElevationList[index] > minHeight:
                end = index
                maxHeight = surfaceElevationList[index]
            else:
                minHeight = surfaceElevationList[index]
        elif surfaceElevationList[index] >= surfaceElevationList[start]:
            end = index
            maxHeight = min(
                surfaceElevationList[start], surfaceElevationList[end])
            for x in range(start+1, end):
                capacity += maxHeight - surfaceElevationList[x]
            # capacityList.append((start,end,maxHeight))
            start = index
            # end = index
    print(capacity)


findWaterCapacity([2, 1, 2])
findWaterCapacity([3, 0, 1, 3, 0, 5])
