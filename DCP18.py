# Hard

# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

#     10 = max(10, 5, 2)
#     7 = max(5, 2, 7)
#     8 = max(2, 7, 8)
#     8 = max(7, 8, 7)

# Do this in O(n) time and O(k) space. You can modify the input array in place and you do not need to store the results. You can simply print them out as you compute them.
from collections import deque


def maxInK(array, k):
    maxStack = deque()
    start = 0
    end = 0
    while end < len(array):
        # print('start is', start)
        # print('end is', end)
        # print('max stack is', maxStack)
        if end < k-1:
            while len(maxStack) != 0 and maxStack[-1] < array[end]:
                maxStack.pop()
                # print('max stack is', maxStack)

            maxStack.append(array[end])
            # print('max stack is', maxStack)
            end += 1

        else:
            # print('max stack is', maxStack)
            while len(maxStack) != 0 and maxStack[-1] < array[end]:
                maxStack.pop()
                # print('max stack is', maxStack)
            maxStack.append(array[end])
            # print('max stack is', maxStack)
            if array[start] == maxStack[0]:
                print(maxStack.popleft())
            else:
                print(maxStack[0])

            end += 1
            start += 1


if __name__ == '__main__':
    maxInK([10, 5, 2, 7, 8, 7, 10, 5, 3, 2, 2, 9, 5], 3)
