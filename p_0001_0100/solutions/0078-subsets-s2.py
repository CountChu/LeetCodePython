solution_json = {
    "date": "2023/12/16",
    "design": 0,
    "coding": 10,
    "runtime": "47 ms",
    "fasterThan": "17%",
    "memory": "16.57 MB"
}

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
lg = print

'''
     0 1 2
    [1 2 3]

     0 0 0   0   []
     0 0 1   1   [1]
     0 1 0   2   
     0 1 1   3
     1 0 0   4
     1 0 1   5
     1 1 0   6
     1 1 1   7

'''

def gen(nums, s):
    out = []
    for i in range(len(s)):
        if s[i] == '1':
            out.append(nums[i])
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        m = 2**n
        #lg(n, m)
        out = []
        for i in range(m, m*2):
            s = bin(i)
            s = s[3:]
            #lg('%3d, %s' % (i, s))
            item = gen(nums, s)
            out.append(item)
        
        return out
