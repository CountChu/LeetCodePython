solution_json = {
    "date": "2024/1/3",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "??%",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"
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

           0  1    2  3  4  5
        [100, 4, 200, 1, 3, 2]
              .       .  .  .

        [0] 100:  {100}
        [1]   4:  {100}, {4}
        [2] 200:  {100}, {4}, {200} 
        [3]   1:  {100}, {4}, {200}, {1}
        [4]   3:  {100}, {4, 3}, {200}, {1}
        [5]   2:  {100}, {4, 3, 2}, {200}

'''

def find_sets(set_ls, v):
    
    out = []
    for set0 in set_ls:
        if v + 1 in set0:
            if set0 not in out:
                out.append(set0)

        if v in set0:
            if set0 not in out:
                out.append(set0)

        if v - 1 in set0:
            if set0 not in out:
                out.append(set0)
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = nums
        n = len(nums)
        set_ls = []
        for i in range(n):
            v = nums[i]

            sets = find_sets(set_ls, v)
            if len(sets) == 2:
                set0, set1 = sets
                set_ls.remove(set0)
                set_ls.remove(set1)
                new_set = set0.union(set1)
                new_set.add(v)
                set_ls.append(new_set)

            elif len(sets) == 1:
                set0 = sets[0]
                set0.add(v)
            
            elif len(sets) == 0:
                set0 = set()
                set_ls.append(set0)
                set0.add(v)

            else:
                assert False, len(sets)

            #lg('[%d] %3d: %s' % (i, v, set_ls))

        out = 0
        for set0 in set_ls:
            out = max(out, len(set0))
        
        return out


