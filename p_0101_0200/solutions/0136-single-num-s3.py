solution_json = {
    "date": "2023/12/23",
    "design": 0,
    "coding": 3,
    "runtime": "99 ms",
    "fasterThan": "99%",
    "memory": "20.39 MB"
}

#
# https://leetcode.com/problems/single-number/
#
# Given a non-empty array of integers nums, every element appears twice except 
# for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity 
# and use only constant extra space.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    [4, 1, 2, 1, 2], 4


    [1 1 2 2 4 4] <- [1 2 4]
    [1 1 2 2 4]

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def singleNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        return 2 * sum(num_set) - sum(nums)
