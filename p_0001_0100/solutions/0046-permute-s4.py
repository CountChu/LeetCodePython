solution_json = {
    "date": "2024/1/9",
    "design": 0,
    "coding": 14,
    "runtime": "33 ms",
    "fasterThan": "97%",
    "memory": "17.49 MB"
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

        (1, 2, 3)
            1, (2, 3)
                2, (3)
                    3  -> [1, 2, 3]
                3, (2)
                    2  -> [1, 3, 2]
            2, (1, 3)
                1, (3)
                    3  -> [2, 1, 3]
                3, (1)
                    1  -> [2, 3, 1]
            3, (1, 2)

         0  1  2  3
        [1, 2, 3, 4]

            ls[0], ls[0:0] + ls[1:]
            ls[1], ls[0:1] + ls[2:]
            ls[2], ls[0:2] + ls[3:]

'''

def split(ls, i):
    v = ls[i]
    ls1 = ls[0:i] + ls[i+1:]
    return v, ls1

def go(ls, n, level, path, out):
    #lg('%sls = %s' % ('    '*level, ls))
    if n == 1:
        path.append(ls[0])
        #lg('%spath = %s' % ('    '*level, path))
        out.append(path.copy())
        path.pop()
        return

    for i in range(n):
        v, ls1 = split(ls, i)
        path.append(v)
        #lg('%s%d, %s' % ('    '*level, v, ls1))
        go(ls1, len(ls1), level+1, path, out)
        path.pop()

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ls = nums
        n = len(ls)
        level = 0
        path = []
        out = []
        go(ls, n, level, path, out)
        return out
