#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.
#
# Example 1:
#       Input: root = [3, 9, 20, null, null, 15, 7]
#       Output: 3
#
# Example 2: 
#       Input: root = [1,null,2]
#       Output: 2
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxDepth(self, root: TreeNode) -> int:   
        pass
