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
    "date": "2022/10/8",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    '''
        indexDiff = 2
        valueDiff = 3

         i     j
         0  1  2  3  4  5
        [1, 5, 9, 1, 5, 9]
    '''
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if j - i <= indexDiff:
                    if abs(nums[i] - nums[j]) <= valueDiff:
                        return True
        return False