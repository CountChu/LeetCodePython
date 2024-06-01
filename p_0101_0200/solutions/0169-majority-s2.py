solution_json = {
    "date": "2023/12/24",
    "design": 0,
    "coding": 6,
    "runtime": "135 ms",
    "fasterThan": "97%",
    "memory": "18.82 MB"
}

#
# https://leetcode.com/problems/majority-element/
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2    
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        out = -1
        h = {}
        for i in range(n):
            v = nums[i]
            if not v in h:
                h[v] = 0
            h[v] += 1

            if out == -1:
                out = v
            elif h[out] < h[v]:
                out = v
        
        return out
