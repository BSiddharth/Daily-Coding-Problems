# Easy

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
class Node:
    def __init__(self, value, right=None, left=None) -> None:
        self.value = value
        self.right = right
        self.left = left


def countUnivalHelper(root):

    if root.left == None and root.right == None:
        return 1
    count = 0
    if root.left != None:
        count += countUnivalHelper(root.left)
    if root.right != None:
        count += countUnivalHelper(root.right)

    if root.left.value == root.right.value:
        count += 1
    return count


def countUnival(root):
    print(countUnivalHelper(root))


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(1)
    # root.right.right = Node(0)
    # root.right.left = Node(1)
    # root.right.left.right = Node(1)
    # root.right.left.left = Node(1)
    countUnival(root)
