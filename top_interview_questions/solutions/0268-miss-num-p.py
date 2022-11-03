#
# https://leetcode.com/problems/missing-number/
#
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/3",
    "design": 0,
    "coding": 3,
    "runtime": "7454 ms",
    "fasterThan": "5%",
    "memory": "15.2 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def missingNumber(self, nums: List[int]) -> int:
        out = None
        for i in range(0, len(nums) + 1):
            if i not in nums:
                out = i
                break
        
        return out







