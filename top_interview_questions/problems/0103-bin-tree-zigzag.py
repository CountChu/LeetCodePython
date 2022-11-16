#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Given the root of a binary tree, return the zigzag level order traversal 
# of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
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

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        pass


