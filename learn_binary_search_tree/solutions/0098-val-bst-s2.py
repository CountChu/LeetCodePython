#
# https://leetcode.com/problems/validate-binary-search-tree/
#
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#       Input: root = [2,1,3]
#       Output: True
#
# Example 2: 
#       Input: [5,1,4,null,null,3,6]
#       Output: False
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/7",
    "design": 0,
    "coding": 0,
    "runtime": "55 ms",
    "fasterThan": "79",
    "memory": "17.1 MB" 
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
    def __init__(self):
        self.val = None 
        self.stop = False

    def go(self, node):
        if self.stop:
            return

        if node.left != None:
            self.go(node.left)

        if self.val != None:
            if self.val >= node.val:
                self.stop = True 
                return
        #print(node.val)
        self.val = node.val 

        if node.right != None:
            self.go(node.right)

    def isValidBST(self, root: TreeNode) -> bool:        
        self.val = None
        self.stop = False

        self.go(root)
        
        return not self.stop 




