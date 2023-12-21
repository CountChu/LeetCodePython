solution_json = {
    "date": "2023/12/20",
    "design": 0,
    "coding": 0,
    "runtime": "348 ms",
    "fasterThan": "99%",
    "memory": "32.68 MB"
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

'''         0  1    2  3  4  5
         [100, 4, 200, 1, 3, 2]
        
    num_set = {1, 2, 3, 100, 4, 200}

    num = 1    .  .  .       .
    num = 2
    num = 3         
    num = 100             .
    num = 4                  
    num = 200                     .   


'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        if len(num_set) == 1:
            return 1

        #lg(num_set)
        count = 0
        out = 0
        for num in num_set:
            #lg('num = %d' % num)
            if num - 1 in num_set:
                continue

            count = 1
            #lg('    count = %d' % count)
            while True:
                if not num + 1 in num_set:
                    break

                num += 1
                count += 1
                #lg('    count = %d' % count)
            
            out = max(out, count)

        return out


        


