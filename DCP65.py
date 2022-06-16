# Easy

# This problem was asked by Amazon.

# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

# For example, given the following matrix:

# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:

# 2 3 1 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = 0
        count = 0
        skip = 0
        move = "r"
        while count < m * n:
            result.append(matrix[x][y])
            count += 1
            if y + skip < n - 1 and move == "r":
                y += 1
                if y + skip == n - 1:
                    move = "d"

            elif y + skip == n - 1 and move == "r":
                x += 1
                move = "d"

            elif x + skip < m - 1 and move == "d":
                x += 1
                if x + skip == m - 1:
                    move = "l"

            elif x + skip == m - 1 and move == "d":
                y -= 1
                move = "l"

            elif y > skip and move == "l":
                y -= 1
                if y == skip:
                    move = "u"
                    skip += 1
            elif x > skip and move == "u":
                x -= 1
                if x == skip:
                    move = "r"

        return result
