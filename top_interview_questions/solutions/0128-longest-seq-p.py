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
    "date": "2022/11/14",
    "design": 0,
    "coding": 0,
    "runtime": "770 ms",
    "fasterThan": "72%",
    "memory": "29 MB" 
}

'''
    [100, 4, 200, 1, 3, 2]

    [1, 2, 3, 4, 100, 200]
        1  1  1   96  100
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(set(nums))
        nums.sort()
        #print(nums)

        d_ls = get_diff_list(nums)
        #print(d_ls)

        out = 0
        count = 0
        state = 'init'
        for d in d_ls:
            if d == 1:
                count += 1
            else:
                out = max(out, count)
                count = 0
            #print(d, count, out)

        out = max(out, count)

        return out + 1

def get_diff_list(nums):
    n = len(nums)
    out = []
    for i in range(1, n):
        v0 = nums[i-1]
        v1 = nums[i]
        out.append(v1 - v0)

    return out

