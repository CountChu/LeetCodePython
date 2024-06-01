#
# https://leetcode.com/problems/jump-game/
#
# You are given an integer array nums. You are initially positioned 
# at the array's first index, and each element in the array represents 
# your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/27",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"    
}

'''
     0  1  2  3  4
    [2, 3, 1, 1, 4]
     2  j  j
        3  j  j  j
           1  j
              1  j

     0  1  2  3  4
    [3, 2, 1, 0, 4]
     3  j  j  j
        2  j  j
           1  j
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ls = [False]*n
        count = 0
        for i in range(n):
            v = nums[i]
            for j in range(i+1, v+i+1):
                if j >= n:
                    break

                if ls[j] == False:
                    ls[j] = True
                    count += 1

        return count == n - 1
        
