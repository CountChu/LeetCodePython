#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T 
# that has both p and q as descendants (where we allow a node to be a descendant 
# of itself).”
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/8",
    "design": 0,
    "coding": 0,
    "runtime": "79 ms",
    "fasterThan": "96%",
    "memory": "18.8 MB" 
}

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    '''
                 6
             2<-     8<- 
           0   4   7   9 
              3 5 
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_nd_ls = find_node_path(root, p.val)
        q_nd_ls = find_node_path(root, q.val)
        #dump(p_nd_ls)
        #dump(q_nd_ls)
        
        n = min(len(p_nd_ls), len(q_nd_ls))
        nd = None
        for i in range(n):
            p_nd = p_nd_ls[i]    
            q_nd = q_nd_ls[i]
            if p_nd.val == q_nd.val:
                nd = p_nd
            else:
                break
        return nd

def find_node_path(root, val):
    nd = root 
    path = [nd]
    while True:
        if nd == None:
            break

        if nd.val == val:
            return path
        elif val < nd.val:
            nd = nd.left 
            path.append(nd)
        else:
            nd = nd.right
            path.append(nd)

    return path

def dump(nd_ls):
    ls = []
    for nd in nd_ls:
        ls.append(nd.val)
    print(ls)


















