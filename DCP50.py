# Easy

# This problem was asked by Microsoft.

# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.


def evaluateTree(treeRoot):
    def helper(treeRoot):
        if not (treeRoot.left and treeRoot.right):
            return treeRoot.val
        if treeRoot.val == "+":
            return helper(treeRoot.left) + helper(treeRoot.right)
        elif treeRoot.val == "-":
            return helper(treeRoot.left) - helper(treeRoot.right)
        elif treeRoot.val == "*":
            return helper(treeRoot.left) * helper(treeRoot.right)
        elif treeRoot.val == "/":
            return helper(treeRoot.left) / helper(treeRoot.right)

    return helper(treeRoot)
