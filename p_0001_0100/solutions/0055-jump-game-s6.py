solution_json = {
    "date": "2024/1/9",
    "design": 0,
    "coding": 6,
    "runtime": "3178 ms",
    "fasterThan": "13.33%",
    "memory": "19.34 MB"
}

#
# https://leetcode.com/problems/jump-game/
#
# Medium.
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
    Input: nums = [2,3,1,1,4]
    Output: true

         0  1  2  3  4
        [2, 3, 1, 1, 4]
            .  .
               .  .  .
                  .  .

    Input: nums = [3,2,1,0,4]
    Output: false

         0  1  2  3  4
        [3, 2, 1, 0, 4]
            .  .  .
               .  .
                  . 

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canJump(self, nums: List[int]) -> bool:
        ls = nums
        n = len(ls)
        set0 = set()
        for i in range(n):
            v = ls[i]
            #lg('v = %d' % v)
            for j in range(i+1, min(i+1+v, n)):
                #lg('%d, ' % j, end='')
                set0.add(j)
                if len(set0) == n - 1:
                    return True                
            #lg('')

        return len(set0) == n - 1

