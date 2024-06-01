solution_json = {
    "date": "2023/12/24",
    "design": 0,
    "coding": 3,
    "runtime": "138 ms",
    "fasterThan": "94%",
    "memory": "18.74 MB"
}

#
# https://leetcode.com/problems/majority-element/
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

        [2, 2, 1, 1, 1, 2, 2]

         0  1  2  3  4  5  6
        [1, 1, 1, 2, 2, 2, 2]
                  .

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = n // 2
        return nums[i]
