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
    "date": "2022/9/7",
    "design": 0,
    "coding": 0,
    "runtime": "56 ms",
    "fasterThan": "26%",
    "memory": "14 MB" 
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
        self.out = []

    def go(self, node):
        if node == None:
            return

        if node.left != None:
            self.go(node.left)

        if node.val != None:
            self.out.append(node.val)

        if node.right != None:
            self.go(node.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.out = []
        self.go(root)

        return self.out 



