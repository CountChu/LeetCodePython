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
    "date": "2022/9/6",
    "design": 0,
    "coding": 0,
    "runtime": "370 ms",
    "fasterThan": "50%",
    "memory": "15.6 MB" 
}

"""
case 1:
    0 1 2 3 4 5 6 7 -
    i       m       j
            4 5 6 7
            i   m   j
            4 5
            i m j

case 2:
     0 1 2 3 4 5 6 -
     i     m       j 
           i   m   j
           i m j

case 3:
     0 1 2 3 4 5 6 -
     i     m       j 
     i m   j
     i j

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0 
        j = len(nums)
        
        while True:
            m = (i + j) // 2
            #print(i, j, m)

            if nums[m] == target:
                return m
            
            elif nums[m] < target:
                i = m 

            else:
                j = m

            if j - i == 2:
                if nums[j-1] == target:
                    return j-1
                if nums[i] == target: 
                    return i
                break 

            if j - i == 1:
                if nums[i] == target:
                    return i
                break

            if j - i == 0:
                break

        return -1
