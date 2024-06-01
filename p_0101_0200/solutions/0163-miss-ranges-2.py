solution_json = {
    "date": "2023/12/24",
    "design": 0,
    "coding": 7,
    "runtime": "37 ms",
    "fasterThan": "63%",
    "memory": "17.33 MB"
}

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
lg = print

'''
    Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
    Output: [[2, 2], [4, 49], [51, 74], [76, 99]]


     0                   99
     0   1   2    3    4   
    [0,  1,  3,  50,  75]
    v0  v1
    

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        n = len(nums)

        if n == 0:
            return [[lower, upper]]

        out = []
        v0 = nums[0]
        if lower < v0:
            #lg(lower, v0-1)
            out.append([lower, v0-1])

        for i in range(1, n):
            v0 = nums[i-1]
            v1 = nums[i]
            #lg(v0, v1)
            if v1 - v0 >= 2:
                #lg(v0+1, v1-1)
                out.append([v0+1, v1-1])

        v1 = nums[n-1]
        if v1 < upper:
            #lg(v1+1, upper)
            out.append([v1+1, upper])

        return out

