#
# https://leetcode.com/problems/symmetric-tree/
#
# Given the root of a binary tree, check whether it is a mirror of itself 
# (i.e., symmetric around its center).
#
# Example 1:
#       Input: root = [1,2,2,3,4,4,3]
#       Output: true
#
# Example 2: 
#       Input: [1,2,2,null,3,null,3]
#       Output: false
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

    def isSymmetric(self, root: TreeNode) -> bool:
        pass     
