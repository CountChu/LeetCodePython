#
# https://leetcode.com/problems/delete-node-in-a-bst/
#
# Given a root node reference of a BST and a key, delete the node 
# with the given key in the BST. Return the root node reference (possibly updated) 
# of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node. 
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

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        pass




