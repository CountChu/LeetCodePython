#
# https://leetcode.com/problems/contains-duplicate-iii/
#
# You are given an integer array nums and two integers indexDiff and valueDiff.
#
# Find a pair of indices (i, j) such that:
#       - i != j,
#       - abs(i - j) <= indexDiff.
#       - abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.
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

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        pass