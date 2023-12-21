solution_json = {
    "date": "2023/12/18",
    "design": 0,
    "coding": 19,
    "runtime": "37 ms",
    "fasterThan": "76%",
    "memory": "17.49 MB"
}

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

'''
    3
        20
            7
            15
        9
            N
            N
    ----

    [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8]
    
    0 
        4
            -1
                8
                N
            3
                6
                N
        2
            N
            1
                1
                5
'''

def go(q, h):
    if q == []:
        return

    nd, level = q.pop(0)
    #lg('%d: %d' % (level, nd.val))
    if level not in h:
        h[level] = []
    h[level].append(nd.val)

    if nd.left != None:
        q.append((nd.left, level+1))

    if nd.right != None:
        q.append((nd.right, level+1))

    go(q, h) 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
            #lg('%d: %s' % (level, ls))
            if level % 2 == 1:
                out.append(ls[::-1])
            else:
                out.append(ls)
        
        return out


