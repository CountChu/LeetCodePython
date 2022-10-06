#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
# You are given a perfect binary tree where all leaves are on the same level, 
# and every parent has two children. The binary tree has the following definition:
#
#   struct Node {
#       int val;
#       Node *left;
#       Node *right;
#       Node *next;
#   }
#
# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.
#
# Example 1:
#       Input: [1,2,3,4,5,6,7]
#       Output: [1,#,2,3,#,4,5,6,7,#]
#
# Example 2: 
#       Input: []
#       Output: []
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

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def connect(self, root: Node) -> Node: 
        pass
