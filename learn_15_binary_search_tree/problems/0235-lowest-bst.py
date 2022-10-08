#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T 
# that has both p and q as descendants (where we allow a node to be a descendant 
# of itself).”
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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass