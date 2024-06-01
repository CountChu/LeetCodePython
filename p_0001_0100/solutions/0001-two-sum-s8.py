solution_json = {
    "date": "2024/5/26",
    "design": 0,
    "coding": 14,
    "runtime": "61 ms",
    "fasterThan": "57%",
    "memory": "17.8 MB"
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

                                c1: v1 in h
                                                   c2: [0, 1] is diff 
        i = 0, v = 2,  v1 = 7,  c1 = X,
        i = 1, v = 7,  v1 = 2,  c1 = V, h[v1] = 0, c2 = V 
        i = 2, v = 11, v1 = -2, 
        i = 3, v = 15, v1 = -6, 

     0  1  2   3
    [2, 5, 5, 11], 10, [1, 2]
        v  v

        i = 0, v = 2,  v1 = 8, c1 = X
        i = 1, v = 5,  v1 = 5, c1 = V, h[v1] = 1, c2 = X
        i = 2, v = 5,  v1 = 5, c1 = V, h[v1] = 1, c2 = V
        i = 3, v = 11,  
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        out = None
        h = {}
        for i, v in enumerate(nums):
            v1 = target - v
            lg(i, v, v1)

            if v not in h:
                h[v] = i
            
            if v1 in h:
                i1 = h[v1]
                if i1 != i:
                    out = [i1, i]
                    break

        return out

