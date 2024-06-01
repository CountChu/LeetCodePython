solution_json = {
    "date": "2024/5/26",
    "design": 0,
    "coding": 37,
    "runtime": "56 ms",
    "fasterThan": "76%",
    "memory": "17.72 MB"
}

#
# https://leetcode.com/problems/two-sum/
#
# Easy.
#
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.  
#

from typing import List
import pdb
br = pdb.set_trace
lg = print

'''
     0  1   2   3
    [2, 7, 11, 15], 9, [0, 1]
     v  v

    0: v1 = 2,  v2 = 7,   h[2]  = 0   
    1: v1 = 7,  v2 = 2,   h[7]  = 1  <--- 
    2: v1 = 11, v2 = -2,  h[11] = 2
    3: v1 = 15, v2 = -6,  h[15] = 3


     0  1  2
    [3, 2, 3], 6, [0, 2]
     v     v

    0, v1 = 3, v2 = 3, h[3] = 0
    1, v1 = 2, v2 = 4, h[2] = 1
    2, v1 = 3, v2 = 3, 3 exists



'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        h = {}
        out = None
        for i1, v1 in enumerate(nums):
            v2 = target - v1
            #lg(i1, v1, v2)

            if v1 not in h:
                h[v1] = i1
                if v2 in h:
                    i2 = h[v2]
                    if i1 != i2:
                        out = [i1, i2]
                        break
            else:
                if v2 in h:
                    i2 = h[v2]
                    if i1 != i2:
                        out = [i1, i2]
                        break

        return out

