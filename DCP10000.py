from copy import copy
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        count = 0
        freshCount = 0

        bufferQ = deque()

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    bufferQ.append([x, y])
                elif grid[x][y] == 1:
                    freshCount += 1

        while len(bufferQ) != 0:
            if freshCount == 0:
                return count
            count += 1
            workingQ = deque()

            while len(bufferQ) != 0:
                el = bufferQ.popleft()
                workingQ.append(el)

            while len(workingQ) != 0:

                currentX, currentY = workingQ.popleft()
                for xMove, yMove in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if (
                        not (
                            (0 > currentX + xMove)
                            or (currentX + xMove >= m)
                            or (currentY + yMove < 0)
                            or (currentY + yMove >= n)
                        )
                    ) and grid[currentX + xMove][currentY + yMove] == 1:

                        grid[currentX + xMove][currentY + yMove] = 2
                        freshCount -= 1

                        bufferQ.append([currentX + xMove, currentY + yMove])

        if freshCount == 0:
            return count

        return -1


# s = Solution()
# print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
