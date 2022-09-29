#
# Build a N-ary Tree for the problem 0589.
#
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
#
# Given an array...
#
# Example 1:
#       Input: ls = [
#           1,
#           None, 3, 2, 4,
#           None, 5, 6
#           ]
#       Output: "1, (3, 2, 4), (5, 6)"
#
# Example 2: 
#       Input: ls = [
#           1,
#           None, 2, 3, 4, 5,
#           None, None, 6, 7, None, 8, None, 9, 10,
#           None, None, 11, None, 12, None, 13, None,
#           None, 14
#       ]
#       Output: "1, (2, 3, 4, 5), (), (6, 7), (8), (9, 10), (), (11), (12), (13), (), (14)"
# 
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
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def ls_to_n_ary_tree(self, ls):
        return Node()

    def n_ary_tree_to_str(self, node):
        return "1, (3, 2, 4), (5, 6)"
