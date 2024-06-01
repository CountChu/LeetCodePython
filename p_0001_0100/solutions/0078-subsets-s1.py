#
# https://leetcode.com/problems/subsets/
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution 
# in any order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/30",
    "design": 0,
    "coding": 0,
    "runtime": "34 ms",
    "fasterThan": "91%",
    "memory": "16.55 MB" 
}

'''
    [0, 1, 2]
     0  0  0    [] 
     0  0  1    [2]
     0  1  0    [1]
     0  1  1    [1, 2]
     1  0  0    [0]
     1  0  1    [0, 2]
     1  1  0    [0, 1]
     1  1  1    [0, 1, 2]
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [[], nums]

        out_ls = []
        for i in range(2**n):
            out = []
            b = bin(i+2**n)
            b = str(b)
            b = b[3:]
            for j in range(len(b)):
                if b[j] == '1':
                    out.append(nums[j])
            #print(out)
            out_ls.append(out)

        return out_ls


