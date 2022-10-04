#
# https://leetcode.com/problems/binary-tree-inorder-traversal/
#
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Example 1:
#       Input: root = [1,null,2,3]
#       Output: [1,3,2]
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
    "date": "2022/10/4",
    "design": 0,
    "coding": 0,
    "runtime": "52 ms",
    "fasterThan": "53%",
    "memory": "13.8 MB" 
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        out = []
        go(root, out)
        return out 

'''
         1
   None      2
            3
'''
def go(nd, out):
    if nd == None:
        return

    go(nd.left, out)
    out.append(nd.val)
    go(nd.right, out)









