# Medium
# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return self.val

    def __repr__(self) -> str:
        return self.val


def serialize(root):
    serializedString = ''
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        currentNode = queue.popleft()
        if currentNode == None:
            serializedString += str(None)
            if len(queue) == 0:
                continue
            serializedString += ' '
            continue
        serializedString += str(currentNode.val)
        serializedString += ' '
        queue.append(currentNode.left)
        queue.append(currentNode.right)
    # print(serializedString)
    return serializedString


def deserialize(serializedString):
    valueList = list(serializedString.split(' '))
    valueQueue = deque(valueList)
    # print('value queue is', valueQueue)
    root = Node(valueQueue.popleft())
    nodeQueue = deque()
    nodeQueue.append(root)
    # print('node queue is', nodeQueue)
    # print('value queue is', valueQueue)

    while len(valueQueue) != 0:
        currentNode = nodeQueue.popleft()
        # print('current node is', currentNode.val)
        # print('node queue is', nodeQueue)
        # print('value queue is', valueQueue)

        currentNode.left = Node(valueQueue.popleft())

        # print('adding', currentNode.left.val)
        nodeQueue.append(currentNode.left)
        # print('node queue is', nodeQueue)
        # print('value queue is', valueQueue)

        currentNode.right = Node(valueQueue.popleft())

        # print('adding', currentNode.right.val)
        nodeQueue.append(currentNode.right)
    #     print('node queue is', nodeQueue)
    # print('root is', root)
    return root


if __name__ == '__main__':
    # node = Node('root', Node('left', Node('left.left')), Node('right'))
    # serialize(node)

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
