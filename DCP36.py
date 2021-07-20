# Medium

# This problem was asked by Dropbox.

# Given the root to a binary search tree, find the second largest node in the tree.

# import math
# from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def findLargest(root):
    currentNode = root
    while currentNode.right != None:
        currentNode = currentNode.right
    return currentNode.val


def findSecondLargest(root):
    currentNode = root
    while currentNode.right != None and currentNode.right.right != None:
        currentNode = currentNode.right
    if currentNode.right == None:
        if currentNode.left == None:
            print('Not Possible')
            return
        else:
            return findLargest(currentNode.left)

    else:
        if currentNode.right.left != None:
            return findLargest(currentNode.right.left)
        else:
            return currentNode.val


root = Node(5)
root.left = Node(6)
root.left.left = Node(3)
root.left.right = Node(7)
root.left.right.right = Node(8)
root.left.left.left = Node(1)
root.left.left.right = Node(5)
root.left.left.right.left = Node(4)
root.left.left.left.left = Node(0)
root.left.left.left.right = Node(2)
print(findSecondLargest(root))
