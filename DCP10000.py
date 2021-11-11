# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, nums: List[int],leftIndex:int,rightIndex:int):
        if rightIndex  <= leftIndex:
            return TreeNode(None)
        print(leftIndex,rightIndex)
        
        maximumIndex = leftIndex
        for x in range(rightIndex-leftIndex+1):
            if nums[leftIndex + x]>nums[maximumIndex]:
                maximumIndex = leftIndex + x
        print(nums[maximumIndex],maximumIndex)
        root = TreeNode(val=nums[maximumIndex],left= self.helper(nums,leftIndex,maximumIndex-1), right=self.helper(nums,maximumIndex+1,rightIndex) )
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.helper(nums,0,len(nums)-1)
        return root

print()
        