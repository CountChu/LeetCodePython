#
# https://leetcode.com/problems/symmetric-tree/
#
# Given the root of a binary tree, check whether it is a mirror of itself 
# (i.e., symmetric around its center).
#
# Example 1:
#       Input: root = [1,2,2,3,4,4,3]
#       Output: true
#
# Example 2: 
#       Input: [1,2,2,null,3,null,3]
#       Output: false
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/5",
    "design": 0,
    "coding": 0,
    "runtime": "42 ms",
    "fasterThan": "82%",
    "memory": "14.1 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    '''
             1
        2         2
     2          2

             0
        1         1
      3   4     4   3
     1 2 3 4   4 3 2 1

             1
         N       2    
               3

    '''
    def isSymmetric(self, root: TreeNode) -> bool:
        nd = root 

        if (nd.left == None) ^ (nd.right == None):
            return False

        if nd.left == None and nd.right == None:
            return True

        q0 = [nd.left]
        q1 = [nd.right]
        while True:
            if q0 == []:
                break 
            if q1 == []:
                break

            nd0 = q0.pop(0)
            nd1 = q1.pop(0)
            #print(nd0.val, nd1.val)
            if nd0.val != nd1.val:
                return False

            if (nd0.left == None) ^ (nd1.right == None):
                return False

            if nd0.left != None:
                q0.append(nd0.left)
            if nd1.right != None:
                q1.append(nd1.right)

            if (nd0.right == None) ^ (nd1.left == None):
                return False

            if nd0.right != None:
                q0.append(nd0.right)
            if nd1.left != None:
                q1.append(nd1.left)

        return True 



















