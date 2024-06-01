solution_json = {
    "date": "2023/12/30",
    "design": 0,
    "coding": 17,
    "runtime": "7165 ms",
    "fasterThan": "5%",
    "memory": "19.29 MB"
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
    Input: nums = [2,3,1,1,4]
    Output: true

         0  1  2  3  4
        [2, 3, 1, 1, 4]
         i  .  .
            i  .  .  .

    Input: nums = [3,2,1,0,4]
    Output: false

         0  1  2  3  4
        [3, 2, 1, 0, 4]
         i  .  .  . 
            i  .  .
               i  .
                  i

    [1,0,2,2,0], False

         0  1  2  3  4
        [1, 0, 2, 2, 0]
         i  .
            i
               i  .  .

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canJump(self, nums: List[int]) -> bool:
        ls = nums
        n = len(ls)
        if n == 1:
            return True

        vis = set()
        for i in range(n - 1):
            v = ls[i]

            end = min(i + 1 + v, n)
            for j in range(i+1, end):
                #lg(i, j)
                vis.add(j)
                if len(vis) == n - 1:
                    return True

        return False
