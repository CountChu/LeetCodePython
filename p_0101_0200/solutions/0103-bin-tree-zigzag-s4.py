solution_json = {
    "date": "2024/1/11",
    "design": 0,
    "coding": 10,
    "runtime": "37 ms",
    "fasterThan": "73%",
    "memory": "17.58 MB"
}

#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Medium.
#
# Given the root of a binary tree, return the zigzag level order traversal 
# of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

        3
            9
                N
                N
            20
                15
                7

'''

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
        while True:
            if q == []:
                break

            nd, level = q.pop(0)
            if level not in h:
                h[level] = []
            h[level].append(nd.val)

            #lg('%s%d' % ('    '*level, nd.val))
            if nd.left != None:
                q.append((nd.left, level+1))
            if nd.right != None:
                q.append((nd.right, level+1))

        out = []
        for level in sorted(h.keys()):
            ls = h[level]
            if level % 2 == 1:
                out.append(ls[::-1])
            else:
                out.append(ls)

        return out

