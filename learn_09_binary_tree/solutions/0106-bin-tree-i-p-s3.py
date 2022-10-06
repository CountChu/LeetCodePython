#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#
# Given two integer arrays inorder and postorder where inorder 
# is the inorder traversal of a binary tree and postorder is the postorder traversal 
# of the same tree, construct and return the binary tree.
#
# Example 1:
#       Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
#       Output: [3,9,20,null,null,15,7]
#
# Example 2: 
#       Input: inorder = [-1], postorder = [-1]
#       Output: [-1]
# 
# Constraints:
#
#       - 1 <= inorder.length <= 3000
#       - postorder.length == inorder.length
#       - -3000 <= inorder[i], postorder[i] <= 3000
#       - inorder and postorder consist of unique values.
#       - Each value of postorder also appears in inorder.
#       - inorder is guaranteed to be the inorder traversal of the tree.
#       - postorder is guaranteed to be the postorder traversal of the tree.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/5",
    "design": 0,
    "coding": 0,
    "runtime": "118 ms",
    "fasterThan": "71%",
    "memory": "18.4 MB" 
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
         0  1   2   3  4
        [9, 3, 15, 20, 7] = inorder
        [9, 15, 7, 20, 3] = postorder
        stack
        [9, 3, 15, 20, 7]

        --------           
            3
        [9]   [15, 20, 7]
        
        [9, 15, 7, 20] = postorder
        stack ---> [9, 3, 15, 20, 7] 
        [15, 20, 7]
        [9]

        --------           
           3
        [9]       20   
              [15]  [7]
        
        [9, 15, 7] = postorder
        stack ---> [15, 20, 7]
        [7]
        [15]
        [9]

        --------           
           3
        [9]       20   
              [15]   7
        
        [9, 15] = postorder
        stack ---> [7]
        [15]
        [9]

        --------           
           3
        [9]       20   
               15   7
        
        [9] = postorder 
        stack ---> [15]
        [9]

        --------           
           3
        9        20   
               15   7
        [] = postorder
        stack ---> [9]
        []

    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:  
        h = {}
        for i, v in enumerate(inorder):
            assert v not in h
            h[v] = i

        nd = TreeNode()
        nd_r = (nd, 0, len(inorder))
        stack = [nd_r]

        head = None
        while True:
            if stack == []:
                break
            #dump_stack(stack)

            nd_r = stack.pop()
            if head == None:
                head = nd_r[0]

            if postorder == []:
                continue 

            v = postorder.pop()
            #print('v = %d' % v)
            nd = nd_r[0]
            nd.val = v 
            left_r, right_r = split(nd_r, h[v])

            if left_r != None:
                nd.left = left_r[0]
                stack.append(left_r)

            if right_r != None:
                nd.right = right_r[0]
                stack.append(right_r)
        
        #br()
        return head

def split(r, idx):
    _, begin, end = r

    if idx == begin:
        left_r = None
    else:
        left_r = (TreeNode(), begin, idx)
    
    if idx + 1 == end:
        right_r = None 
    else:
        right_r =  (TreeNode(), idx + 1, end)
    
    return left_r, right_r

def dump_stack(stack):
    ls = []
    for nd, begin, end in stack:
        ls.append((begin, end))
    print(ls)






