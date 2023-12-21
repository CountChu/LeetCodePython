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
    "date": "2023/12/6",
    "design": 0,
    "coding": 0,
    "runtime": "35 ms",
    "fasterThan": "74%",
    "memory": "16.34 MB" 
}

'''
    nums  0 1 3 50 75
    lower = 0   -> -1
    upper = 99  -> 100
    
    0 1 2 3  4  5   6

   -1 0 1 3 50 75 100
      1 1 2 47 25  25
          . .  .    .

'''

lg = print
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[int]:
        nums.append(lower - 1)
        nums.append(upper + 1)
        nums = list(set(nums))
        nums.sort()
        #lg(nums)

        out = []
        n = len(nums)
        for i in range(1, n):
            v0 = nums[i-1]
            v1 = nums[i]
            if v1 - v0 >=2:
                #lg(v0+1, v1-1)
                out.append([v0+1, v1-1])

        return out
