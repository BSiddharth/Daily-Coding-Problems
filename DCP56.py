# Medium

# This problem was asked by Google.

# Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        if len(paths) == 0:
            return [1 for _ in range(n)]
        adjacencyListDict = {}
        result = [None for _ in range(n)]

        for path in paths:

            fromNode = path[0]
            toNode = path[1]

            if fromNode not in adjacencyListDict:
                adjacencyListDict[fromNode] = set()

            if toNode not in adjacencyListDict:
                adjacencyListDict[toNode] = set()

            adjacencyListDict[fromNode].add(toNode)
            adjacencyListDict[toNode].add(fromNode)

        for node in range(1, n + 1):
            if node not in adjacencyListDict:
                result[node - 1] = 1
            else:
                for color in range(1, 5):
                    if all(
                        result[neighbours - 1] != color
                        for neighbours in adjacencyListDict[node]
                    ):
                        result[node - 1] = color
                        break
        return result
