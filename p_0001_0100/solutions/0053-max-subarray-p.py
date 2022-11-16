#
# https://leetcode.com/problems/maximum-subarray/
#
# Given an integer array nums, find the subarray which has the largest sum 
# and return its sum.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/9",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded" 
}

'''
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                .   .  .  .    
     -2 -1  -4  0  -1  1  2  -3  1  i = 0
         1  -2  2   1  3  4  -1  3  i = 1
            -3  1   0  2  3  -2  2  i = 2
                4   3  5  6   1  5  i = 3
                   -1  1  2  -3  1  i = 4
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ls = [0] * n
        acc = 0
        for i, v in enumerate(nums):
            acc += v 
            ls[i] = acc
        #print('ls = %s' % ls)
        max_idx = arg_max(ls)
        out = ls[max_idx]
        #print('max_idx = %d' % max_idx)

        for i in range(1, n):
            d = nums[i] - ls[i]
            max_idx = arg_max(ls[i:]) + i
            max_v = ls[max_idx] + d
            #print('max_idx = %d, max_v = %d' % (max_idx, max_v))
            out = max(out, max_v)
        
        return out

def arg_max(ls):
    out = -1
    max_v = None
    for i, v in enumerate(ls):
        if max_v == None:
            max_v = v
            out = i
        else:
            if max_v < v:
                max_v = v
                out = i
    return out
