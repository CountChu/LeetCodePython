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
    "date": "2023/11/29",
    "design": 0,
    "coding": 0,
    "runtime": "48 ms",
    "fasterThan": "12.76",
    "memory": "16.38 MB" 
}

'''
    [2 0 2 1 1 0]
'''

def reach(h, v):
    while True:

        if h[v] != 0:
            return v

        v += 1

    return None

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
    Do not return anything, modify nums in-place instead.
    """
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        h = {0:0, 1:0, 2:0}
        for v in nums:
            h[v] += 1

        v = 0
        for i in range(n):
            v = reach(h, v)
            nums[i] = v
            h[v] -= 1
