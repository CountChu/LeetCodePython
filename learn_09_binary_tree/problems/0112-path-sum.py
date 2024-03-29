#
# https://leetcode.com/problems/path-sum/
#
# Given the root of a binary tree and an integer targetSum, return true 
# if the tree has a root-to-leaf path such that adding up all the values 
# along the path equals targetSum.
#
# A leaf is a node with no children.
#
# Example 1:
#       Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#       Output: true
#
# Example 2: 
#       Input: root = [1,2,3], targetSum = 5
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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:   
        return False   
