solution_json = {
    "date": "2024/1/3",
    "design": 0,
    "coding": 8,
    "runtime": "335 ms",
    "fasterThan": "98%",
    "memory": "32.6 MB"
}

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
lg = print

'''
    Input: nums = [100,4,200,1,3,2]
    Output: 4

                {1, 2, 3, 4, 100, 200}
        1:       .  .  .  .
        2:       
        3:
        100:                   .
        4:
        200:                       .


'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestConsecutive(self, nums: List[int]) -> int:
        set0 = set(nums)
        out = 0
        for v in set0:
            #lg('%d:' % v)
            if v - 1 in set0:
                continue
        
            #lg('    .')
            i = 1
            while True:
                if v + i not in set0:
                    break
                i += 1
                #lg('    .') 
            out = max(out, i)

        return out


