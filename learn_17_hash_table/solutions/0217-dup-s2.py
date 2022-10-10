#
# https://leetcode.com/problems/contains-duplicate/
#
# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.
#
# Example 1:
#       Input: nums = [1,2,3,1]
#       Output: true
#
# Example 2: 
#       Input: nums = [1,2,3,4]
#       Output: false
# 
# Example 3: 
#       Input: nums = [1,1,1,3,3,4,3,2,4,2]
#       Output: true
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/10",
    "design": 0,
    "coding": 0,
    "runtime": "463 ms",
    "fasterThan": "96%",
    "memory": "26 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for v in nums:
            if v in num_set:
                return True
            num_set.add(v)

        return False
