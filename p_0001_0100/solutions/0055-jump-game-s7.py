solution_json = {
    "date": "2024/1/15",
    "design": 0,
    "coding": 13,
    "runtime": "2280 ms",
    "fasterThan": "15%",
    "memory": "19.72 MB"
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
            .  .          i = 0, v = 2 -> 1, 2 -> {1, 2}
               .  .  .    i = 1, v = 3 -> 2, 3, 4 -> {1, 2, 3, 4}


    Input: nums = [3,2,1,0,4]
    Output: false

         0  1  2  3  4
        [3, 2, 1, 0, 4]
            .  .  .      i = 0
               .  .      i = 1
                  .      i = 2
                         i = 3

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canJump(self, nums: List[int]) -> bool:
        ls = nums
        n = len(ls)

        if n == 1:
            return True

        fill = set()
        for i in range(1, n):
            fill.add(i)
        #br()

        set0 = set()
        for i in range(n - 1):
            v = ls[i]
            #lg('[%d] %d' % (i, v))
            for j in range(i+1, i+1+v):
                set0.add(j)
                #lg(set0)
                if set0 == fill:
                    return True
        
        return False
