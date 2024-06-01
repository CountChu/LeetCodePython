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

solution_json = {
    "date": "2023/12/6",
    "design": 0,
    "coding": 0,
    "runtime": "190 ms",
    "fasterThan": "18%",
    "memory": "18.46 MB" 
}

'''
    [4 1 2 1 2]

     0 1 2 3 4
    [1 1 2 2 4]

     1 [1 2 2 4]  

'''

lg = print
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        v = nums.pop(0)
        while True:
            if len(nums) == 0:
                break

            v1 = nums.pop(0)
            #lg(v, v1, nums)
            if v == v1:
                v = None 
            elif v == None:
                v = v1
            else:
                break

        return v
