solution_json = {
    "date": "2023/12/15",
    "design": 0,
    "coding": 9,
    "runtime": "6198 ms",
    "fasterThan": "5.88%",
    "memory": "17.99 MB"
}

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
lg = print

'''
           0 1 2 3 4
    nums: [2 3 1 1 4]
           i . .
             i . . .
               i .
                 i . 

        h[1] = 1
        h[2] = 2
        h[3] = 1
        h[4] = 1


           0 1 2 3 4
    nums: [3 2 1 0 4]
           i . . .
             i . .
               i 

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        h = {}
        for i in range(n - 1):
            #lg(i)
            v = nums[i]
            for j in range(i+1, i+1+v):
                if j == n:
                    break
                #lg('    ', j)
                
                if j not in h:
                    h[j] = 0
                h[j] += 1

            if len(h) == n - 1:
                return True 

        if len(h) == n - 1:
            return True 
        else:
            return False




