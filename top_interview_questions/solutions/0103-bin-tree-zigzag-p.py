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

solution_json = {
    "date": "2022/11/14",
    "design": 0,
    "coding": 10,
    "runtime": "59 ms",
    "fasterThan": "60%",
    "memory": "14.2 MB" 
}

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

        nd = root
        level = 0
        q = [(nd, level)]

        h = {}
        while True:
            if q == []:
                break

            nd, level = q.pop(0)
            #print(nd.val, level)
            if level not in h:
                h[level] = []
            h[level].append(nd.val)

            if nd.left != None: 
                q.append((nd.left, level+1))

            if nd.right != None:
                q.append((nd.right, level+1))    

        out = []
        for level, v_ls in h.items():
            if level % 2 == 1:
                r_v_ls = reverse(v_ls)
                #print(level, r_v_ls)
                out.append(r_v_ls)
            else:
                #print(level, v_ls)
                out.append(v_ls)

        return out

def reverse(ls):
    out = []
    for i in reversed(range(len(ls))):
        out.append(ls[i])
    return out


