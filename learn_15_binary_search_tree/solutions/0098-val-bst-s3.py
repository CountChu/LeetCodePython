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
    "date": "2022/10/7",
    "design": 0,
    "coding": 0,
    "runtime": "33 ms",
    "fasterThan": "99%",
    "memory": "17.2 MB" 
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
    def isValidBST(self, root: TreeNode) -> bool:
        ctx = {
            'ls': [],
            'out': True
        }
        go(root, ctx)
        return ctx['out']

def go(nd, ctx):
    if nd == None:
        return 

    go(nd.left, ctx)
    #print(nd.val)
    if ctx['ls'] != []:
        if ctx['ls'][-1] >= nd.val:
            ctx['out'] = False 
            return

    ctx['ls'].append(nd.val)

    go(nd.right, ctx)






