# Medium

# This problem was asked by Amazon.

# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        currentSumWithLastElementIncluded = 0

        for x in nums:
            currentSumWithLastElementIncluded = x + (
                currentSumWithLastElementIncluded
                if currentSumWithLastElementIncluded > 0
                else 0
            )
            maxSum = max(maxSum, currentSumWithLastElementIncluded)
        return maxSum
