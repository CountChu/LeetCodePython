#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
#
# Given a binary tree
#   struct Node {
#       int val;
#       Node *left;
#       Node *right;
#       Node *next;
#   }
#
# Example 1:
#       Input: [1,2,3,4,5,null,7]
#       Output: [1,#,2,3,#,4,5,7,#]
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
