# Hard

# This problem was asked by Dropbox.

# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

# Implement an efficient sudoku solver.


from typing import List
import copy


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        validators = {}
        emptyCoordinates = []
        for x in range(9):
            validators["row" + str(x)] = set()
            validators["col" + str(x)] = set()
            validators["box" + str(x)] = set()

        for x in range(9):
            for y in range(9):
                if 0 <= x <= 2 and 0 <= y <= 2:
                    box = "box0"
                elif 0 <= x <= 2 and 3 <= y <= 5:
                    box = "box1"
                elif 0 <= x <= 2 and 6 <= y <= 8:
                    box = "box2"
                elif 3 <= x <= 5 and 0 <= y <= 2:
                    box = "box3"
                elif 3 <= x <= 5 and 3 <= y <= 5:
                    box = "box4"
                elif 3 <= x <= 5 and 6 <= y <= 8:
                    box = "box5"
                elif 6 <= x <= 8 and 0 <= y <= 2:
                    box = "box6"
                elif 6 <= x <= 8 and 3 <= y <= 5:
                    box = "box7"
                elif 6 <= x <= 8 and 6 <= y <= 8:
                    box = "box8"

                if board[x][y] == ".":
                    emptyCoordinates.append((x, y, box))
                else:
                    validators["row" + str(x)].add(board[x][y])
                    validators["col" + str(y)].add(board[x][y])
                    validators[box].add(board[x][y])

        def helper(board, validators, emptyCoordinates):

            if len(emptyCoordinates) == 0:

                return True
            emptyX, emptyY, box = emptyCoordinates.pop()

            for val in range(1, 10):

                if (
                    (str(val) not in validators["row" + str(emptyX)])
                    and (str(val) not in validators["col" + str(emptyY)])
                    and (str(val) not in validators[box])
                ):

                    validatorsCopy = copy.deepcopy(validators)
                    validatorsCopy["row" + str(emptyX)].add(str(val))
                    validatorsCopy["col" + str(emptyY)].add(str(val))
                    validatorsCopy[box].add(str(val))
                    emptyCoordinatesCopy = copy.deepcopy(emptyCoordinates)
                    board[emptyX][emptyY] = str(val)

                    if helper(board, validatorsCopy, emptyCoordinatesCopy):
                        return True
                    board[emptyX][emptyY] = "."
            return False

        helper(board, validators, emptyCoordinates)


# board = [
#     [".", ".", ".", "2", ".", ".", ".", "6", "3"],
#     ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
#     [".", ".", "1", ".", ".", "3", "9", "8", "."],
#     [".", ".", ".", ".", ".", ".", ".", "9", "."],
#     [".", ".", ".", "5", "3", "8", ".", ".", "."],
#     [".", "3", ".", ".", ".", ".", ".", ".", "."],
#     [".", "2", "6", "3", ".", ".", "5", ".", "."],
#     ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
#     ["4", "7", ".", ".", ".", "1", ".", ".", "."],
# ]
# s = Solution()
# s.solveSudoku(board)
# print(board)
