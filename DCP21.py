# Easy

# This problem was asked by Snapchat.

# Given an array of time intervals(start, end) for classroom lectures(possibly overlapping), find the minimum number of rooms required.

# For example, given[(30, 75), (0, 50), (60, 150)], you should return 2.


def howManyRooms(timingList):
    startList = [x[0] for x in timingList]
    endList = [x[1] for x in timingList]
    startList.sort()
    endList.sort()
    startIndex = 0
    endIndex = 0
    currentRooms = 0
    maxRooms = 0

    while startIndex < len(timingList):
        if startList[startIndex] < endList[endIndex]:
            currentRooms += 1
            maxRooms = max(maxRooms, currentRooms)
            startIndex += 1
        else:
            currentRooms -= 1
            endIndex += 1
    print(maxRooms)


if __name__ == '__main__':
    howManyRooms([(5, 7), (0, 9), (5, 9)])
