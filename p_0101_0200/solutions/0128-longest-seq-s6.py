solution_json = {
    "date": "2024/1/22",
    "design": 0,
    "coding": 18,
    "runtime": "343 ms",
    "fasterThan": "90%",
    "memory": "31.8 MB"
}

#
# https://leetcode.com/problems/longest-consecutive-sequence/
#
# Medium.
#
# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence.
#
# You must write an a#lgorithm that runs in O(n) time.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
    Input: nums = [100,4,200,1,3,2]
    Output: 4

         0  1  2  3    4    5
        [1, 2, 3, 4, 100, 200]

                   i = 0, v = ls[i]
        [0] 1    : v,   i = 0
        [1] 2    : v+1, i = 1
        [2] 3    : v+2, i = 2
        [3] 4    : v+3, i = 3
                   v+4 -> i = 4, v = 100
        [4] 100  : 
        [5] 200  :

    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9

        [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]

    [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7

          0   1  2  3  4  5  6  7  8  9 10
        [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        ls = nums
        set0 = set(ls)
        ls = sorted(ls)
        #lg(ls)
        n = len(ls)

        i = 0
        v = ls[i]
        out = 0
        count = 0
        while True:
            if i == n:
                out = max(out, count)
                break

            if v in set0:
                #lg('[%d]: v = %d' % (i, v))
                v += 1
                i += 1
                count += 1
            else:
                #lg('-')
                out = max(out, count)
                count = 0
                v = ls[i]

        return out

        pass


