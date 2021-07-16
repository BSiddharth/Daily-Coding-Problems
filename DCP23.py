# Easy

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [ [f, f, f, f],
#   [t, t, f, t],
#   [f, f, f, f],
#   [f, f, f, f], ]

# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

import math
from collections import deque


def maxSteps(map, source, target):
    distanceMatrix = [[math.inf for x in range(
        len(map[0]))] for x in range(len(map))]
    distanceMatrix[source[0]][source[1]] = 0
    print('distance matrix is', distanceMatrix)
    queue = deque()
    queue.append(source)
    print('queue is', queue)

    combinatons = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while len(queue) != 0:
        currentPoint = queue.pop()
        print('currentPoint is', currentPoint)
        x = currentPoint[0]
        y = currentPoint[1]
        for combination in combinatons:
            if 0 <= x + combination[0] < len(map) and 0 <= y + combination[1] < len(map[0]) and map[x + combination[0]][y + combination[1]] == 'f' and distanceMatrix[x + combination[0]][y + combination[1]] == math.inf:
                print('currentPoint added is', currentPoint)
                queue.append((x + combination[0], y + combination[1]))
                distanceMatrix[x + combination[0]][y +
                                                   combination[1]] = distanceMatrix[x][y]+1

    if distanceMatrix[target[0]][target[1]] == math.inf:
        print(None)
    else:
        print(distanceMatrix[target[0]][target[1]])


if __name__ == '__main__':
    f = 'f'
    t = 't'
    maxSteps([[f, f, f, f],
              [t, t, f, t],
              [f, f, f, f],
              [f, f, f, f], ], (3, 0), (0, 0))
