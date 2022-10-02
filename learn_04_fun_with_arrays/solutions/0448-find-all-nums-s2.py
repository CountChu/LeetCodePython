#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
#
# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.
#
# Example 1:
#       Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
#       Output: [5, 6]
#
# Example 2: 
#       Input: nums = [1, 1]
#       Output: [2]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/2",
    "design": 0,
    "coding": 0,
    "runtime": "500 ms",
    "fasterThan": "68%",
    "memory": "26.4 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        h = {}                          # h[i] = False
        for i in range(n):
            h[i+1] = False 

        for v in nums:
            h[v] = True

        out = []
        for idx, occurred in h.items():
            if not occurred:
                out.append(idx) 
        
        return out
