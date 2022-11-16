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
    "date": "2022/11/12",
    "design": 0,
    "coding": 9,
    "runtime": "56 ms",
    "fasterThan": "71%",
    "memory": "14.2 MB" 
}

'''
    [1]
    [], [1]

    [1, 2]
    []:   [2]
    [1]:  [1, 2]

    [1, 2, 3]
    []           -> [3]
    [1]          -> [1, 3]
    [2]          -> [2, 3]
    [1, 2, 3]    -> [1, 2, 3, 4]
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        v = nums[0] 
        out = [[], [v]]

        for i in range(1, len(nums)):
            out = gen(out, nums[i])

        return out

def gen(ls_ls, v):
    new_ls_ls = []
    for ls in ls_ls:
        new_ls_ls.append(ls + [v])

    out = ls_ls + new_ls_ls
    return out


