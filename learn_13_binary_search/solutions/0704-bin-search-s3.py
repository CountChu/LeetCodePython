#
# https://leetcode.com/problems/binary-search/
#
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
#       Input: nums = [-1,0,3,5,9,12], target = 9
#       Output: 4
#
# Example 2: 
#       Input: nums = [-1,0,3,5,9,12], target = 2
#       Output: -1
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "697 ms",
    "fasterThan": "5%",
    "memory": "15.5 MB" 
}

'''
      i     k     v  j
      0  1  2  3  4  5
    [-1, 0, 3, 5, 9, 12]
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ctx = {
            'out': -1
        }
        func(nums, 0, len(nums) - 1, target, ctx)
        return ctx['out']

def func(nums, i, j, target, ctx):
    k = (i + j) // 2
    #print(i, k, j)
    if ctx['out'] != -1:
        return

    if i > j:
        return

    if nums[k] == target:
        ctx['out'] = k
        return
    elif nums[k] < target:
        i = k + 1
        func(nums, i, j, target, ctx)
    else:
        j = k - 1
        func(nums, i, j, target, ctx)
