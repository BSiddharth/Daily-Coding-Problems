# Medium

# This problem was asked by Facebook.

# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

#       Right, then down
#       Down, then right

# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.


from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moveList = [(1, 0), (0, 1)]

        @cache
        def helper(currentNode):

            if currentNode[0] == m - 1 and currentNode[1] == n - 1:
                return 1
            result = 0
            for move in moveList:
                if (
                    0 <= currentNode[0] + move[0] < m
                    and 0 <= currentNode[1] + move[1] < n
                ):

                    result += helper(
                        (currentNode[0] + move[0], currentNode[1] + move[1])
                    )
            return result

        return helper((0, 0))


s = Solution()
print(s.uniquePaths(3, 7))
