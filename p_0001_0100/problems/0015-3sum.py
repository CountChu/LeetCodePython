#
# https://leetcode.com/problems/3sum/
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
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

''' 
      0  1  2  3   4   5 
    [-1, 0, 1, 2, -1, -4]

    -4: [5]
    -1: [0, 4]
     0: [1]
     1: [2]
     2: [3]

     -1+0 = -1  (0, 1)
     -1+1 = 0   (0, 2)
     -1+2 = 1   (0, 3)
     -1-1 = -2  (0, 4)
     -1-4 = -5  (0, 5)

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass
