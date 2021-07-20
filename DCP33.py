# Hard

# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

class SortedArray:
    def __init__(self, values=[]) -> None:
        values.sort()
        self.internalList = values

    def add(self, value):
        print('inserting', value)
        length = len(self.internalList)
        if length == 0:
            self.internalList.append(value)
            return
        else:
            for i in range(length):
                if self.internalList[i] > value:
                    self.internalList.insert(i, value)
                    print('list is', self.internalList)

                    return
        self.internalList.append(value)
        print('list is', self.internalList)

    def findMedian(self):
        length = len(self.internalList)
        print('length is', length)
        if length % 2 == 0:
            print((self.internalList[int((length/2)-1)] +
                   self.internalList[int((length/2))])/2)
        else:
            print(self.internalList[int(((length+1)/2)-1)])


def findMedian(inputList):
    sortedList = SortedArray()
    for x in inputList:
        sortedList.add(x)
        sortedList.findMedian()


findMedian([2, 1, 5, 7, 2, 0, 5])
