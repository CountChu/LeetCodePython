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
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        pass
