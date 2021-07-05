# Hard
# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def findMissing(arr):
    arrLen = len(arr)
    firstPositiveIndex = None
    for index in range(arrLen):
        if arr[index] > 0:
            firstPositiveIndex = index
            break
    if firstPositiveIndex == None:
        print(1)
        return
    currentIndex = 0
    while currentIndex <= arrLen - 1:
        # print(arr)
        if currentIndex == firstPositiveIndex:

            currentIndex += 1
        elif currentIndex < firstPositiveIndex:
            if arr[currentIndex] <= 0:
                currentIndex += 1

            else:
                arr[firstPositiveIndex -
                    1], arr[currentIndex] = arr[currentIndex], arr[firstPositiveIndex-1]
                arr[firstPositiveIndex], arr[firstPositiveIndex -
                                             1] = arr[firstPositiveIndex-1], arr[firstPositiveIndex]
                firstPositiveIndex -= 1
        else:
            if arr[currentIndex] > 0:
                currentIndex += 1
            else:
                arr[firstPositiveIndex +
                    1], arr[currentIndex] = arr[currentIndex], arr[firstPositiveIndex+1]
                arr[firstPositiveIndex], arr[firstPositiveIndex +
                                             1] = arr[firstPositiveIndex+1], arr[firstPositiveIndex]
                firstPositiveIndex += 1
    arr = arr[firstPositiveIndex:]
    # print(arr)
    arrLen -= firstPositiveIndex

    for index in range(arrLen):
        if abs(arr[index]) <= arrLen:
            arr[abs(arr[index])-1] = -arr[abs(arr[index])-1]
    for index in range(arrLen):
        if arr[index] > 0:
            print(index+1)
            return
    print(arrLen+1)


if __name__ == '__main__':
    findMissing([3, 4, -1, 1])
    findMissing([1, 2, 0])
    findMissing([-1, -5, -6])
    findMissing([-1, -5, -6, 1, 3, 6, 2, 5])
