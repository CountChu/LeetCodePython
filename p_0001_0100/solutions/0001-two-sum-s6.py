solution_json = {
    "date": "2023/12/13",
    "design": 0,
    "coding": 12,
    "runtime": "68 ms",
    "fasterThan": "54%",
    "memory": "17.54 MB"
}

#
# https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.  
#

from typing import List
import pdb
br = pdb.set_trace

'''
     0 1 2  3
    [2 5 5 11]  10
     i = 0, v0 = 2, v1 = 8, v1 not in h, h[2] = 0 
     i = 1, v0 = 5, v1 = 5, v1 not in h, h[5] = 0
     i = 2, v0 = 5, v1 = 5, v1 in h, return h[v1], i  

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        n = len(nums)
        h = {}
        for i in range(n):
            v0 = nums[i]
            v1 = target - v0
            if v1 in h:
                return [h[v1], i] 
            else:
                h[v0] = i

        return None

