#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Given the root of a binary tree, return the zigzag level order traversal 
# of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

solution_json = {
    "date": "2023/12/2",
    "design": 0,
    "coding": 0,
    "runtime": "40 ms",
    "fasterThan": "56%",
    "memory": "17.59 MB" 
}

'''
       1
    2    3
  4  N  N  5


            3
        9     20
       N N   15 7


                0
         2               4
      1     N        3       -1
    5   1          N   6    N   8  

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def go(q, h):
    if len(q) == 0:
        return

    nd, level = q.pop(0)
    #lg(level, nd.val)
    if level not in h:
        h[level] = []
    h[level].append(nd.val) 

    if nd.left != None:
        q.append((nd.left, level+1))

    if nd.right != None:
        q.append((nd.right, level+1))

    go(q, h)

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        q = [(root, 0)]
        h = {}
        go(q, h)

        out = []
        for level, ls in h.items():
            if level % 2 == 1:
                ls = ls[::-1]
            out.append(ls)

        return out


