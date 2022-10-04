#
# https://leetcode.com/problems/binary-tree-level-order-traversal/
#
# Given the root of a binary tree, return the level order traversal 
# of its nodes' values. (i.e., from left to right, level by level).
#
# Example 1:
#       Input: root = [3,9,20,null,null,15,7]
#       Output: [[3],[9,20],[15,7]]
#
# Example 2: 
#       Input: root = [1]
#       Output: [[1]]
# 
# Example 3: 
#       Input: root = []
#       Output: []
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/4",
    "design": 0,
    "coding": 0,
    "runtime": "44 ms",
    "fasterThan": "79%",
    "memory": "14.9 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    '''
             3
         9      20  
             15    17
    '''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:   
        if root == None:
            return []

        q = [root]
        out = []
        go(q, out)  
        return out


def go(q, out):
    #dump_q(q)
    if q == []:
        return

    v_ls = [nd.val for nd in q]
    out.append(v_ls)
    q2 = []
    for nd in q:
        #print(nd.val)
        if nd.left != None:
            q2.append(nd.left)
        if nd.right != None:
            q2.append(nd.right)

    go(q2, out)

def dump_q(q):
    v_ls = [nd.val for nd in q]
    print(v_ls)





