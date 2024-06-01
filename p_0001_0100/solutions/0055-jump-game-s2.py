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
    "date": "2022/11/27",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

'''
    ChatGPT solution:

     0  1  2  3  4
    [2, 3, 1, 1, 4]
 f   0  2  4  4 
     2  4  3  4


     0  1  2  3  4
    [3, 2, 1, 0, 4]
     0  3  3  3 
     3  3  3  3

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(n - 1):
            print(i, farthest, i + nums[i])
            if farthest == n - 1: # my optimization
                return True

            farthest = max(farthest, i + nums[i])
            if farthest <= i:
                return False
        return farthest >= n - 1


