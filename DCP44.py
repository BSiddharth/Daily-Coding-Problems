# Medium

# This problem was asked by Google.

# We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.


class Solution:
    def inversion(self, nums):

        inversionCount = 0

        def helper(l):

            nonlocal inversionCount
            if len(l) == 1:

                return l
            mid = len(l) // 2
            left = l[:mid]
            right = l[mid:]

            leftSorted = helper(left)
            rightSorted = helper(right)

            i = 0
            j = 0

            sortedList = []
            while i < len(leftSorted) and j < len(rightSorted):
                if leftSorted[i] < rightSorted[j]:
                    sortedList.append(leftSorted[i])
                    i += 1
                else:
                    sortedList.append(rightSorted[j])
                    j += 1
                    inversionCount += len(leftSorted) - i
            while i < len(leftSorted):
                sortedList.append(leftSorted[i])
                i += 1
            while j < len(rightSorted):
                sortedList.append(rightSorted[j])
                j += 1

            return sortedList

        helper(nums)

        return inversionCount
