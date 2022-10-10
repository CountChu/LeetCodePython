#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth 
# of the two subtrees of every node never differs by more than one.
#
# Constraints:
#
#       - 1 <= nums.length <= 104
#       - -104 <= nums[i] <= 104
#       - nums is sorted in a strictly increasing order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/9",
    "design": 0,
    "coding": 0,
    "runtime": "172 ms",
    "fasterThan": "7%",
    "memory": "15.7 MB" 
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
       0   1  2  3  4
    [-10, -3, 0, 5, 9]

              0
         -3       9
     -10       5 

     0  1 
    [1, 3]
    

    '''
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        root = build(nums)
        return root

def build(ls):
    if ls == []:
        return None

    left_ls, v, right_ls = split(ls)
    #print(v)
    nd = TreeNode(v)

    left_nd = build(left_ls)
    nd.left = left_nd

    right_nd = build(right_ls)
    nd.right = right_nd 

    #print(v, '----')

    return nd

def split(ls):
    m = len(ls) // 2
    v = ls[m]
    left_ls = ls[:m]
    right_ls = ls[m+1:]
    return left_ls, v, right_ls




