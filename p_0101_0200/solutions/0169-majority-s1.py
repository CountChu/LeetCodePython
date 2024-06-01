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

solution_json = {
    "date": "2023/12/7",
    "design": 0,
    "coding": 0,
    "runtime": "174 ms",
    "fasterThan": "5.1%",
    "memory": "17.89 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        h = {}
        max_count = None
        out = None
        for i in range(n):
            v = nums[i]
            if v not in h:
                h[v] = 0 
            h[v] += 1

            if max_count == None:
                max_count =  h[v]
                out = v
            else:
                if max_count < h[v]:
                    max_count = h[v]
                    out = v

        return out
