solution_json = {
    "date": "2024/1/10",
    "design": 0,
    "coding": 5,
    "runtime": "26 ms",
    "fasterThan": "99%",
    "memory": "17.44 MB"
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
#lg = print

'''
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

def gen_ls(ls, s):
    out = []
    for i in range(len(s)):
        if s[i] == '1':
            out.append(ls[i])
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = nums
        n = len(ls)
        m = 2**n
        out = []
        for i in range(m):
            s = bin(m+i)
            s = s[3:]
            #lg(s)
            ls1 = gen_ls(ls, s)
            #lg(ls1)
            out.append(ls1)
        return out
