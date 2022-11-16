#
# https://leetcode.com/problems/permutations/
#
# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/8",
    "design": 0,
    "coding": 12,
    "runtime": "85 ms",
    "fasterThan": "35%",
    "memory": "14.1 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ls_ls = []
        for v in nums:
            if ls_ls == []:
                ls_ls = [[v]]
            else:
                new_ls_ls = []
                for ls in ls_ls:
                    new_ls_ls += gen(ls, v)
                ls_ls = new_ls_ls

        return ls_ls

def split(ls, idx):
    return ls[0:idx], ls[idx:]

def gen(ls, v):
    out = []
    for i in range(0, len(ls) + 1):
        ls0, ls1 = split(ls, i)
        new_ls = ls0 + [v] + ls1
        out.append(new_ls)
        #print(new_ls)
    
    return out
