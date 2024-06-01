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
# Constraints:
#       -10^9 <= lower <= upper <= 10^9
#       0 <= nums.length <= 100
#       lower <= nums[i] <= upper
#       All the values of nums are unique.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/2",
    "design": 0,
    "coding": 0,
    "runtime": "53 ms",
    "fasterThan": "57%",
    "memory": "14 MB" 
}

'''
     0  1  2   3   4
    [0, 1, 3, 50, 75] 
     0                 99
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[int]:
        if nums == []:
            if upper - lower == 0:
                return [[1, 1]]
            else:
                return [[lower, upper]]

        out = []

        v1 = nums[0]
        if lower < v1:
            if v1 - lower == 1:
                out.append([lower, lower])
            else:
                out.append([lower, v1-1])

        for i in range(1, len(nums)):
            v0 = nums[i-1]
            v1 = nums[i]

            if v1 - v0 == 1:
                continue 
            
            else:
                v0 += 1
                v1 -= 1
                if v0 == v1:
                    out.append([v0, v0])
                else:
                    out.append([v0, v1])

        v0 = nums[-1]
        if v0 < upper:
            if upper - v0 == 1:
                out.append([upper, upper])
            else:
                out.append([v0+1, upper])

        return out












