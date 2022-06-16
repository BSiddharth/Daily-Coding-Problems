# Easy

# This problem was asked by Microsoft.

# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.


# code is correct but tle in leetcode

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(x, y, i, visited):
            if i >= len(word):
                return True
            if (x, y) in visited:
                return False
            if (
                not (0 <= x < len(board))
                or not (0 <= y < len(board[0]))
                or board[x][y] != word[i]
            ):
                return False
            # print(x, y, visited)
            visitedCopy = visited.copy()
            visitedCopy.add((x, y))
            return (
                helper(x + 1, y, i + 1, visitedCopy)
                or helper(x, y + 1, i + 1, visitedCopy)
                or helper(x, y - 1, i + 1, visitedCopy)
                or helper(x - 1, y, i + 1, visitedCopy)
            )

        for x in range(len(board)):
            for y in range(len(board[0])):
                # print("iiiiiiiiiiii")
                if helper(x, y, 0, set()):
                    return True
        return False


# s = Solution()
# print(s.exist([["a", "a", "a"], ["A", "A", "A"], ["a", "a", "a"]], "aAaaaAaaA"))
