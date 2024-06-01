solution_json = {
    "date": "2023/12/23",
    "design": 0,
    "coding": 4,
    "runtime": "120 ms",
    "fasterThan": "77%",
    "memory": "19.3 MB"
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
    [2, 2, 1] -> 1

     0  1  2  3  4
    [4, 1, 2, 1, 2], 4

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        for v in nums:
            if v not in h:
                h[v] = 0
            h[v] += 1 
        
        for v in h:
            if h[v] == 1:
                return v 

        return -1