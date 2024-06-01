solution_json = {
    "date": "2024/1/12",
    "design": 0,
    "coding": 13,
    "runtime": "?? ms",
    "fasterThan": "??%",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"
}

#
# https://leetcode.com/problems/longest-consecutive-sequence/
#
# Medium.
#
# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: nums = [100,4,200,1,3,2]
    Output: 4
        
           0  1    2  3  4  5
        [100, 4, 200, 1, 3, 2]

        {100, 4, 200, 1, 3, 2}

        [0] 100: 1
        [1]   4: 1 
        [2] 200: 1
        [3]   1: 4
        [4]   3: 2
        [5]   2: 3


'''

def count_it(set0, v0):
    v = v0
    out = 0
    while True:
        if v in set0:
            out += 1
        else:
            break
        v += 1

    return out


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestConsecutive(self, nums: List[int]) -> int:
        ls = nums
        n = len(ls)
        set0 = set(ls)
        out = 0
        for i in range(n):
            v = ls[i]
            c = count_it(set0, v)
            #lg('[%d] %d: %d' % (i, v, c))
            out = max(out, c)

        return out


