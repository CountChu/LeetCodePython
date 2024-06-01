solution_json = {
    "date": "2024/1/9",
    "design": 0,
    "coding": 9,
    "runtime": "41 ms",
    "fasterThan": "78%",
    "memory": "17.26 MB"
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
        1, [1, 2, 3]
            1 X
            2, [1, 2, 3]
                1
                2
                3 
            3, [1, 2, 3]
        2, [1, 2, 3]
            1
            2
            3
        3, [1, 2, 3]
            1
            2
            3
'''

def go(ls, n, level, set0, path, out):
    #lg('%sls = %s' % ('    '*level, ls))

    if len(path) == n:
        #lg('%spath = %s' % ('    '*level, path))
        out.append(list(path))
        return

    for i in range(n):
        v = ls[i]
        if v in path:
            continue

        set0.add(v)
        path.append(v)
        go(ls, n, level+1, set0, path, out)
        set0.remove(v)
        path.pop()


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ls = nums
        n = len(ls)
        level = 0
        set0 = set()
        path = []
        out = []
        go(ls, n, level, set0, path, out)
        
        return out
