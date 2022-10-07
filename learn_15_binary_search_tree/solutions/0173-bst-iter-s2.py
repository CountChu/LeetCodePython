#
# https://leetcode.com/problems/binary-search-tree-iterator/
#
# Implement the BSTIterator class that represents an iterator 
# over the in-order traversal of a binary search tree (BST):.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/7",
    "design": 0,
    "coding": 0,
    "runtime": "178 ms",
    "fasterThan": "14%",
    "memory": "20 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
          7
      3       15
            9   20
'''
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.v_ls = []
        go(root, self.v_ls)        

    def next(self) -> int:
        return self.v_ls.pop(0)

    def hasNext(self) -> bool:
        return self.v_ls != []

    def dump(self):
        print(self.v_ls)

def go(nd, v_ls):
    if nd == None:
        return
    
    go(nd.left, v_ls)
    #print(nd.val)
    v_ls.append(nd.val)
    go(nd.right, v_ls)

#
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()  
#





