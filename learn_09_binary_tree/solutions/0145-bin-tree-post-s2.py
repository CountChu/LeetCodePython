#
# https://leetcode.com/problems/binary-tree-postorder-traversal/#
#
# Given the root of a binary tree, return the postorder traversal of its nodes' values. 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/4",
    "design": 0,
    "coding": 0,
    "runtime": "55 ms",
    "fasterThan": "42%",
    "memory": "13.8 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:      
        out = []
        go(root, out)
        return out

def go(nd, out):
    if nd == None:
        return

    go(nd.left, out)
    go(nd.right, out)
    out.append(nd.val)
