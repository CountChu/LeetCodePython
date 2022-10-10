#
# https://leetcode.com/problems/balanced-binary-tree/
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ 
# in height by no more than 1.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/8",
    "design": 0,
    "coding": 0,
    "runtime": "51 ms",
    "fasterThan": "96%",
    "memory": "18.6 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
         3        
     9      20   
          15  17

                 1
             2       2  
           3   3
          4 4

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True

        ctx = {
            'out': True
        }
        go(root, ctx)
        return ctx['out']

def go(nd, ctx):
    if ctx['out'] == False:
        return 0

    if nd == None:
        return 0

    #print(nd.val)

    left_h = 1 + go(nd.left, ctx)
    right_h = 1 + go(nd.right, ctx)
    if abs(left_h - right_h) >= 2:
        ctx['out'] = False

    #print('....', nd.val, left_h, right_h)
    return max(left_h, right_h)
