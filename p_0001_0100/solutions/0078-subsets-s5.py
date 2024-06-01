solution_json = {
    "date": "2024/1/17",
    "design": 0,
    "coding": 7,
    "runtime": "42 ms",
    "fasterThan": "45%",
    "memory": "17.41 MB"
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
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        n = 3
        2**n = 8

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = nums
        n = len(ls)
        m = 2**n
        b_ls = []
        for i in range(m):
            b = bin(m+i)[3:]
            b_ls.append(b)

        out_ls = []
        for b in b_ls:
            out = []
            for i in range(n):
                if b[i] == '1':
                    out.append(ls[i])
            out_ls.append(out)
        #lg(out_ls)
        return out_ls
