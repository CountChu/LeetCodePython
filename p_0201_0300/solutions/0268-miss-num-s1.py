solution_json = {
    "date": "2023/12/10",
    "design": 0,
    "coding": 0,
    "runtime": "116 ms",
    "fasterThan": "91%",
    "memory": "18.28 MB"
}

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
lg = print

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        for i in range(n + 1):
            if i not in s:
                return i 
        return -1







