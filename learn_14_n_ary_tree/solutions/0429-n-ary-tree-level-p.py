#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal, 
# each group of children is separated by the null value (See examples).
#
# Example 1:
#       Input: root = [
#           1,
#           null, 3, 2, 4,
#           null, 5, 6
#           ]
#       Output: [[1],[3,2,4],[5,6]]
#
# Example 2: 
#       Input: [
#           1,
#           null, 2, 3, 4, 5,
#           null, null, 6, 7, null, 8, null, 9, 10,
#           null, null, 11, null, 12, null, 13, null,
#           null,14
#       ]
#       Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/?26",
    "design": 0,
    "coding": 0,
    "runtime": "114 ms",
    "fasterThan": "21%",
    "memory": "16.2 MB" 
}

#
# Definition for a Node.
#

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []

        nd = root

        h = {}                          # h[level] = v_ls
        q = [(0, nd)]                   # q = [(level, nd)]
        #print(0, '%s' % [nd.val])
        h[0] = [nd.val]

        while True:
            if q == []:
                break 

            (level, nd) = q.pop(0)
            if nd.children == None:
                continue

            v_ls = []
            for child in nd.children:
                v_ls.append(child.val)
            
            if v_ls != []:
                level += 1
                #print(level, v_ls)
                if level not in h:
                    h[level] = []
                h[level] += v_ls

            for child in nd.children:
                q.append((level, child))

        out = list(h.values())
        return out 
