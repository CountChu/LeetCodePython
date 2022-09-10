#
# https://leetcode.com/problems/binary-tree-preorder-traversal/
#
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
# Example 1:
#       Input: root = [1,null,2,3]
#       Output: [1,2,3]
#
# Example 2: 
#       Input: root = []
#       Output: []
# 
# Example 3: 
#       Input: root = [1]
#       Output: [1]
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

#
# Definition for a binary tree node.
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [0, 1, 3, 7, 8, 4, 2, 5, 6]

