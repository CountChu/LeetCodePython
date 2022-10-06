#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes 
# in the tree.
#
# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”
#
# Example 1:
#       Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#       Output: 3
#
# Example 2: 
#       Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#       Output: 5
# 
# Example 3: 
#       Input: root = root = [1,2], p = 1, q = 2
#       Output: 1
#
# Constraints:
#       - The number of nodes in the tree is in the range [2, 10^5].
#       - -10^9 <= Node.val <= 10^9
#       - All Node.val are unique.
#       - p != q
#       - p and q will exist in the tree.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/5",
    "design": 0,
    "coding": 0,
    "runtime": "77 ms",
    "fasterThan": "89%",
    "memory": "25.8 MB" 
}

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None

'''
         3
    5         1
  6   2     0   8
     7 4 
    
    p = 5 -> [3, 5] 
    q = 1 -> [3, 1]
    
    p = 5 -> [3, 5]
    q = 4 -> [3, 5, 2, 4]

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ctx = {
            'path': [],
            'p_val': p.val,
            'q_val': q.val,
            'p_path': None,
            'q_path': None,
            }

        go(root, ctx)
        p_path = ctx['p_path']
        q_path = ctx['q_path']
       
        min_n = min(len(p_path), len(q_path))
        out = None
        for i in range(min_n):
            if p_path[i].val == q_path[i].val:
                out = p_path[i]

        return out 

def go(nd, ctx):
    if nd == None:
        return

    #print(nd.val)
    
    ctx['path'].append(nd)
    #dump_nd_ls(ctx['path'])

    if nd.val == ctx['p_val']:
        ctx['p_path'] = ctx['path'].copy()

    if nd.val == ctx['q_val']:
        ctx['q_path'] = ctx['path'].copy()

    go(nd.left, ctx)
    go(nd.right, ctx)  

    ctx['path'].pop()

def dump_nd_ls(nd_ls):
    ls = []
    for nd in nd_ls:
        ls.append(nd.val)
    print(ls)









