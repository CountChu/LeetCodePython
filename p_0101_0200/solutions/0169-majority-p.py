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
    "date": "2022/11/2",
    "design": 0,
    "coding": 7,
    "runtime": "500 ms",
    "fasterThan": "8%",
    "memory": "15.6 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def majorityElement(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        h = {}
        out = None

        for i, v in enumerate(nums):
            if v not in h:
                h[v] = 0

            h[v] += 1
            if h[v] > n:
                out = v
                break
        
        return out
