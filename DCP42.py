# Hard

# This problem was asked by Google.

# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        memoryCells = [[None for _ in range(len(candidates) + 1)] for _ in range(target + 1)]
        # for x in range(target + 1):
        #     memoryCells[x][0] = False
        for y in range(len(candidates) + 1):
            memoryCells[0][y] = True
        for x in range(1,target + 1):
            for y in range(1,len(candidates) + 1):
                memoryCells[x][y] = memoryCells[x-candidates[y-1]][y] or memoryCells[x][y-1]
        print(memoryCells)

        