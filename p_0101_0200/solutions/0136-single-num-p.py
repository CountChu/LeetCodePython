#
# https://leetcode.com/problems/single-number/
#
# Given a non-empty array of integers nums, every element appears twice except 
# for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity 
# and use only constant extra space.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/31",
    "design": 0,
    "coding": 0,
    "runtime": "301 ms",
    "fasterThan": "51%",
    "memory": "17.2 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def singleNumber(self, nums: List[int]) -> int:
        box = set()
        for v in nums:
            if v not in box:
                box.add(v)
            else:
                box.remove(v)
        
        out = box.pop()
        return out