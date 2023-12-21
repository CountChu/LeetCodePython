#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/25",
    "design": 0,
    "coding": 0,
    "runtime": "79 ms",
    "fasterThan": "83%",
    "memory": "17.75 MB" 
}

'''
            0  1  2  3  4   5
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    searchRange(nums, target) = [3, 4]

    h1[5] = 0
    h1[7] = 1
    h2[7] = 2
    ...
'''


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h1 = {} 
        h2 = {}
        for i in range(n):
            v = nums[i]
            if v not in h1:
                h1[v] = i 
            else:
                h2[v] = i 

        if target in h1:
            if target in h2:
                return [h1[target], h2[target]]
            else:
                return [h1[target], h1[target]]
        else:
            return [-1, -1]





