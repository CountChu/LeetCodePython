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
    "date": "2022/11/7",
    "design": 0,
    "coding": 4,
    "runtime": "632 ms",
    "fasterThan": "27%",
    "memory": "15.5 MB" 
}

'''
          0  1  2  3  4  5
        [-1, 0, 3, 5, 9, 12], target = 9
          i     k        j
                   i  k  j
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        j = n - 1

        while True:
            if i > j:
                break

            k = (i + j) // 2
            if nums[k] == target:
                return k
            elif nums[k] < target:
                i = k + 1
            else:
                j = k - 1

        return -1

