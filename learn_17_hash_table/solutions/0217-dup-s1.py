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
    "date": "2022/9/20",
    "design": 0,
    "coding": 0,
    "runtime": "535 ms",
    "fasterThan": "79%",
    "memory": "25.7 MB" 
}

def cal_idx(n, value):
    idx = value % n
    return idx

def check_value(b, value):
    idx = cal_idx(len(b), value)
    found = False
    for v in b[idx]:
        if v == value:
            found = True 
            break
    return found, idx

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def containsDuplicate(self, nums: List[int]) -> bool:
        n = 1000
        b = [[] for _ in range(n)]
        for v in nums:
            found, idx = check_value(b, v)
            if found:
                return True 

            b[idx].append(v)

        return False



