#
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated 
# at an unknown pivot index k (1 <= k < nums.length) such that the resulting 
# array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 
# and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/25",
    "design": 0,
    "coding": 0,
    "runtime": "54 ms",
    "fasterThan": "15%",
    "memory": "16.91 MB" 
}
'''
     0  1  2  3  4  5  6 
    [4, 5, 6, 7, 0, 1, 2]

    search(nums, 0) = 4
    h[4] = 0 
    h[5] = 1 
    ... 
    h[0] = 4
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def search(self, nums: List[int], target: int) -> int:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        
        if target in h:
            return h[target]

        return -1


     
