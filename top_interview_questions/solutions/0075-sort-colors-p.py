#
# https://leetcode.com/problems/sort-colors/
#
# Given an array nums with n objects colored red, white, or blue, sort them 
# in-place so that objects of the same color are adjacent, with the colors 
# in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, 
# and blue, respectively.
#
# You must solve this problem without using the library's sort function.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/12",
    "design": 0,
    "coding": 7,
    "runtime": "67 ms",
    "fasterThan": "41%",
    "memory": "14 MB" 
}

'''
        [2, 0, 2, 1, 1, 0]
        0: 2
        1: 2
        2: 2
        [0, 0, 1, 1, 2, 2]
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
    Do not return anything, modify nums in-place instead.
    """
    def sortColors(self, nums: List[int]) -> None:
        h = {0: 0, 1: 0, 2: 0}
        for v in nums:
            h[v] += 1

        idx = 0
        idx = fill(nums, idx, 0, h[0])
        idx = fill(nums, idx, 1, h[1])
        idx = fill(nums, idx, 2, h[2])

        return nums

def fill(nums, idx, v, c):
    for i in range(c):
        nums[idx] = v
        idx += 1
    return idx






