#
# https://leetcode.com/problems/search-in-a-binary-search-tree/
#
# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val 
# and return the subtree rooted with that node. 
#
# If such a node does not exist, return null.
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

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        pass




