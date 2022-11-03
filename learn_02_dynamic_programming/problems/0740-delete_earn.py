#
# https://leetcode.com/problems/delete-and-earn/
#
# You are given an integer array nums. You want to maximize the number of points 
# you get by performing the following operation any number of times:
#
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, 
# you must delete every element equal to nums[i] - 1 and every element equal 
# to nums[i] + 1.
#
# Return the maximum number of points you can earn by applying 
# the above operation some number of times.
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

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def deleteAndEarn(self, nums: List[int]) -> int:
        pass