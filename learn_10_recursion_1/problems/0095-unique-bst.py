#
# https://leetcode.com/problems/unique-binary-search-trees-ii/
#
# Given an integer n, return all the structurally unique BST's (binary search trees), 
# which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
#
# Example 1:
#       Input: n = 3
#       Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
# Example 2: 
#       Input: n = 1
#       Output: [[1]]
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

    def generateTrees(self, n: int) -> List[TreeNode]:
        pass
