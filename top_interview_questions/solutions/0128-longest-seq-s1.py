#
# https://leetcode.com/problems/longest-consecutive-sequence/
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

solution_json = {
    "date": "2023/12/4",
    "design": 0,
    "coding": 0,
    "runtime": "368 ms",
    "fasterThan": "94%",
    "memory": "31.99 MB" 
}

'''
    [100, 4, 200, 1, 3, 2]

     0 1 2 3   4.  5
    [1 2 3 4 100 200]
       0 0 0   1   2

    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

     0 1 2 3 4 5 6 7 8 9
    [0 0 1 2 3 4 5 6 7 8]
       0 0 0 0 0 0 0 0 0

    [0 1 1 2]


'''

lg = print
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = list(set(nums))
        nums.sort()
        #lg(nums)

        n = len(nums)
        h = {}
        j = 0
        h[j] = 1
        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                h[j] += 1
            else:
                j += 1 
                h[j] = 1
        #lg(h)

        out = None
        for k, v in h.items():
            if out == None:
                out = v

            out = max(out, v)

        return out

