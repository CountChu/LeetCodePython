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
    "date": "2022/10/5",
    "design": 0,
    "coding": 0,
    "runtime": "41 ms",
    "fasterThan": "97%",
    "memory": "15 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:   
        ctx = {
            'target': targetSum,
            'out': False
        }
        acc = 0
        go(root, acc, ctx)

        return ctx['out'] 

def go(nd, acc, ctx):
    if nd == None:
        return

    if ctx['out'] == True:
        return 

    #print(nd.val)
    acc += nd.val

    if nd.left == None and nd.right == None:
        if acc == ctx['target']:
            ctx['out'] = True 
            return 

    go(nd.left, acc, ctx)
    go(nd.right, acc, ctx)


