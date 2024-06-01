solution_json = {
    "date": "2023/12/25",
    "design": 0,
    "coding": 4,
    "runtime": "109 ms",
    "fasterThan": "98%",
    "memory": "18.46 MB"
}

#
# https://leetcode.com/problems/missing-number/
#
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    [3, 0, 1]
    [0, 1, 2, 3]

    ((1+3) * 3) / 2 = 6

'''

'''


'''


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def missingNumber(self, nums: List[int]) -> int:
        sum0 = sum(nums)
        n = len(nums)
        sum1 = (1 + n) * n // 2
        return sum1 - sum0    






