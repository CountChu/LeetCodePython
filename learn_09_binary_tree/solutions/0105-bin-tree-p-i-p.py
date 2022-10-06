#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# Given two integer arrays preorder and inorder where preorder 
# is the preorder traversal of a binary tree and inorder 
# is the inorder traversal of the same tree, construct 
# and return the binary tree.#
#
# Example 1:
#       Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#       Output: [3,9,20,null,null,15,7]
#
# Example 2: 
#       Input: preorder = [-1], inorder = [-1]
#       Output: [-1]
#
# Constraints:
#       - 1 <= preorder.length <= 3000
#       - inorder.length == preorder.length
#       - -3000 <= preorder[i], inorder[i] <= 3000
#       - preorder and inorder consist of unique values.
#       - Each value of inorder also appears in preorder.
#       - preorder is guaranteed to be the preorder traversal of the tree.
#       - inorder is guaranteed to be the inorder traversal of the tree.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/5",
    "design": 0,
    "coding": 0,
    "runtime": "124 ms",
    "fasterThan": "79%",
    "memory": "18.5 MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    [3, 9, 20, 15, 7] = preorder
    [9, 3, 15, 20, 7] = inorder
    --------
    stack
        [9, 3, 15, 20, 7]
    --------
          3 
     [9]     [15, 20, 7]
    3 <- preorder.pop(0) 
    stack
        [9]
        [15, 20, 7]
    --------
          3
      9       [15, 20, 7]
    9 <- preorder.pop(0)
    stack
        [15, 20, 7]
    --------
          3
      9          20
            [15]    [7]
    20 <- preorder.pop(0)
    stack 
        [15]
        [17]
    --------
          3
      9          20
            15       [7]
    15 <- preorder.pop(0)
    stack
        [17]
    --------
          3
      9          20
             15       7
    7 <- preorder.pop(0)
    stack
        []
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        h = {}
        for i, v in enumerate(inorder):
            assert v not in h
            h[v] = i

        nd_r = (TreeNode(), 0, len(preorder))
        stack = [nd_r]

        head = None
        while True:
            if stack == []:
                break

            v = preorder.pop(0)
            #print('%d --------' % v)

            nd_r = stack.pop()
            if head == None: 
                head = nd_r[0]
            nd_r[0].val = v 

            left_r, right_r = split(nd_r, h[v])
            
            if right_r != None:
                nd_r[0].right = right_r[0]
                stack.append(right_r)

            if left_r != None:
                nd_r[0].left = left_r[0]
                stack.append(left_r)

            #dump_stack(stack)

        return head

def split(nd_r, idx):
    _, begin, end = nd_r
    
    if begin == idx:
        left_r = None 
    else:
        left_r = (TreeNode(), begin, idx)
    
    if idx + 1 == end:
        right_r = None 
    else:
        right_r = (TreeNode(), idx + 1, end)
    
    return left_r, right_r

def dump_stack(stack):
    for nd, begin, end in stack:
        print('(%d, %d)' % (begin, end))














