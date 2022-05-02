# Medium

# This problem was asked by Google.

# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # helper function that will be called recursively and will return the root
        def helper(preorder, inorder):
            if len(preorder) == 0:
                return
            root = TreeNode(preorder[0])
            rootIndex = 0
            while inorder[rootIndex] != preorder[0]:
                rootIndex += 1
            root.left = helper(preorder[1 : 1 + rootIndex], inorder[:rootIndex])
            root.right = helper(preorder[1 + rootIndex :], inorder[rootIndex + 1 :])

            return root

        return helper(preorder, inorder)
