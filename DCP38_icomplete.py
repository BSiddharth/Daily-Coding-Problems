# Hard

# This problem was asked by Microsoft.

# You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

# https://www.dailycodingproblem.com/blog/an-introduction-to-backtracking/

def is_safe(chessBoard, row, col, n):
    #  we dont need to check the col and anything right cuz these is nothing there
    for i in range(col):
        if chessBoard[row][i] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if chessBoard[i][j] == 1:
            return False
    for i, j in zip(range(row+1, n), range(col-1, -1, -1)):
        if chessBoard[i][j] == 1:
            return False
    return True


def numOfArrangementsHelper(n, chessBoard, col):
    count = 0
    if col >= n:
        count += 1
        return count
    for row in range(n):
        if is_safe(chessBoard, row, col, n):
            chessBoard[row][col] = 1
            # newChessBoard = chessBoard.copy()
            newCount = numOfArrangementsHelper(n, chessBoard, col+1)
            if newCount == 0:
                chessBoard[row][col] = 0
            else:
                count += newCount

        # else:
        #     return 0
    return count


def numOfArrangements(n):
    chessBoard = [[0 for x in range(n)] for x in range(n)]
    # count = 0
    print(numOfArrangementsHelper(n, chessBoard, 0))


numOfArrangements(10)
