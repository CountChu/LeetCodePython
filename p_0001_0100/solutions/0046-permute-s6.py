solution_json = {
    "date": "2024/1/14",
    "design": 0,
    "coding": 13,
    "runtime": "44 ms",
    "fasterThan": "61%",
    "memory": "17.42 MB"
}

#
# https://leetcode.com/problems/permutations/
#
# Medium.
#
# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        [1, 2, 3]
            1, [2, 3]
                2, [3]
                    3   -> 1, 2, 3   
                3, [2]
                    2   -> 1, 3, 2
            2, [1, 3]
                1, [3]
                    3
                3, [1]
                    1
            3  [1, 2]

'''

def split(ls, n, idx):
    out_v = None
    out_ls = []
    for i in range(n):
        if i == idx:
            out_v = ls[i]
        else:
            out_ls.append(ls[i])

    return out_v, out_ls

def go(ls, level, path, out):
    #lg('%s%s' % ('    '*level, ls))
    n = len(ls)
    if n == 1:
        v = ls[0]
        path.append(v)
        out.append(path.copy())
        path.pop()
        return

    for i in range(n):
        v, ls1 = split(ls, n, i)
        path.append(v)
        go(ls1, level + 1, path, out)
        path.pop()

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ls = nums
        level = 0
        path = []
        out = []
        go(ls, level, path, out)
        
        return out
