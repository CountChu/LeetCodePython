solution_json = {
    "date": "2023/12/28",
    "design": 0,
    "coding": 16,
    "runtime": "38 ms",
    "fasterThan": "90%",
    "memory": "17.26 MB"
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
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


    (1, 2, 3)
        1 -> (2, 3)
            2 -> (3)
                3 -> ()
            3 -> (2)
                2 -> ()
        2 -> (1, 3)
            1
                3
            3
                2
        3 -> (1, 2)
            1
                3
            2
                1
'''

def go(ls, level, path, out):
    if len(path) == len(ls):
        #lg(path)
        out.append(path.copy())
        return

    n = len(ls)
    for i in range(n):
        v = ls[i]
        if v not in path:
            path.append(v)
            #lg('%s%d' % (' '*level*4, v))
            go(ls, level+1, path, out)
            path.pop()        

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ls = nums
        path = []
        out = []
        go(ls, 0, path, out)

        return out



