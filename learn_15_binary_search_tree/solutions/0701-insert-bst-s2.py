#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
#
# You are given the root node of a binary search tree (BST) and a value 
# to insert into the tree. Return the root node of the BST 
# after the insertion. It is guaranteed that the new value does not exist 
# in the original BST.
#
# Notice that there may exist multiple valid ways for the insertion, 
# as long as the tree remains a BST after insertion. 
# You can return any of them.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/7",
    "design": 0,
    "coding": 0,
    "runtime": "175 ms",
    "fasterThan": "77%",
    "memory": "16.9 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
         4
    2         7
 1    3
 insert 5      

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)

        nd = root
        head = root
        while True:
            if nd == None:
                break

            if nd.val < val:
                if nd.right == None:
                    nd.right = TreeNode(val)
                    break
                else:
                    nd = nd.right 
            elif nd.val > val:
                if nd.left == None:
                    nd.left = TreeNode(val)
                    break
                else:
                    nd = nd.left 
            else:
                assert False
        return head


