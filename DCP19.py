# Medium

# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.


def minCost(costMatrix, totalHouses):

    for x in range(1, totalHouses):
        for y in range(len(costMatrix[0])):
            if y > 0 and y != len(costMatrix[0])-1:
                costMatrix[x][y] = costMatrix[x][y] + min(min([x for x in costMatrix[x-1][0:y]]), min([
                                                          x for x in costMatrix[x-1][y+1:]]))
            elif y == 0:
                costMatrix[x][y] = costMatrix[x][y] + \
                    min(costMatrix[x-1][y+1:])
            elif y == len(costMatrix[0])-1:
                costMatrix[x][y] = costMatrix[x][y] + min(costMatrix[x-1][0:y])
    print(min(costMatrix[-1]))


if __name__ == '__main__':
    minCost([[1, 4, 3], [2, 5, 6], [1, 2, 3], [7, 4, 4]], 4)
