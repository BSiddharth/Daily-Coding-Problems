# Medium

# This problem was asked by Facebook.

# Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.


# ---------------------------------------------------------------Leetcode---------------------------------------------------------------

# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        target = totalSum / 2

        @cache
        def helper(target, currentIndex, currentSum):

            if currentIndex >= len(nums):
                return False

            if currentSum + nums[currentIndex] == target:
                return True

            return helper(
                target, currentIndex + 1, currentSum + nums[currentIndex]
            ) or helper(target, currentIndex + 1, currentSum)

        return helper(target, 0, 0)
