solution_json = {
    "date": "2023/12/14",
    "design": 0,
    "coding": 10,
    "runtime": "43 ms",
    "fasterThan": "71%",
    "memory": "16.36 MB"
}

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
lg = print

'''
            0 1 2
    nums:  [1 2 3]   

              []
      1       2       3      
    2   3   1   3   1   2   
    3   2   3   1   2   1 

'''

def perm(v, ls, path, out):
    if v != None:
        #lg(v)
        path.append(v)

    if len(ls) == 0:
        #lg(path)        
        out.append(path.copy())
        return

    for v in ls:
        ls1 = ls.copy()
        ls1.remove(v)
        #lg(ls1)
        perm(v, ls1, path, out)
        path.pop()

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        out = []
        perm(None, nums, path, out)
        return out
