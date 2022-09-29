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
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "248 ms",
    "fasterThan": "95%",
    "memory": "15.4 MB" 
}

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1 
        
        while True:

            m = (i + j) // 2

            if nums[m] == target:
                return m 
            
            elif nums[m] < target:
                i = m + 1 

            else:  # target < nums[m]
                j = m - 1 

            if i > j:
                break

        return -1