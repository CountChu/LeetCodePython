solution_json = {
    "date": "2023/12/31",
    "design": 0,
    "coding": 8,
    "runtime": "74 ms",
    "fasterThan": "5%",
    "memory": "17.53 MB"
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
        2**3 = 8
        0, 1, 2, 3, ... 7

'''

def gen(n, ls):
    m = 2**n
    out_ls = []
    for i in range(2**n):
        bin_s = bin(m+i)
        bin_s = bin_s[3:]
        #lg(bin_s)
        out = []
        for j in range(len(bin_s)):
            b = bin_s[j]
            if b == '1':
                out.append(ls[j])
        out_ls.append(out)
    return out_ls

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = nums
        n = len(ls)
        out = gen(n, ls)
        return out

