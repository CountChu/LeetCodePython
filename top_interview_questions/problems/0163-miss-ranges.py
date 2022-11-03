#
# https://leetcode.com/problems/missing-ranges/
#
# You are given an inclusive range [lower, upper] and a sorted unique integer 
# array nums, where all elements are in the inclusive range.
#
# A number x is considered missing if x is in the range [lower, upper] 
# and x is not in nums.
# 
# Return the smallest sorted list of ranges that cover every missing number exactly. 
# That is, no element of nums is in any of the ranges, and each missing number 
# is in one of the ranges.
#
# Each range [a,b] in the list should be output as:
#       "a->b" if a != b
#       "a" if a == b
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

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        pass
