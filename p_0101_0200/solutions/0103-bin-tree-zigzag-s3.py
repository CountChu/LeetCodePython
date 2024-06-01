solution_json = {
    "date": "2024/1/2",
    "design": 0,
    "coding": 13,
    "runtime": "41 ms",
    "fasterThan": "51%",
    "memory": "17.5 MB"
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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

        3
            20
                17
                15
            9
                N
                N


'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        level = 0
        q = [(root, level)]

        h = {}
        while True:
            if q == []:
                break

            nd, level = q.pop(0)
            #lg('%s%d' % ('    '*level, nd.val))
            if level not in h:
                h[level] = []
            h[level].append(nd.val)

            if nd.left != None:
                q.append((nd.left, level+1))
            if nd.right != None:
                q.append((nd.right, level+1))        
            
        out = []
        for level, ls in h.items():
            if level % 2 == 1:
                ls = ls[::-1]
            out.append(ls)

        return out
