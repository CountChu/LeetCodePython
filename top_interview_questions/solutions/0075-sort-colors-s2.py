
solution_json = {
    "date": "2023/12/16",
    "design": 0,
    "coding": 0,
    "runtime": "39 ms",
    "fasterThan": "72%",
    "memory": "16.35 MB"
}

#
# https://leetcode.com/problems/sort-colors/
#
# Given an array nums with n objects colored red, white, or blue, sort them 
# in-place so that objects of the same color are adjacent, with the colors 
# in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, 
# and blue, respectively.
#
# You must solve this problem without using the library's sort function.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
       0  1  2  3  4  5
    [  2  0  2  1  1  0]    -- 1
      p0             p2        
       i
    [  0  0  2  1  1  2]
      p0          p2        -- 2
       i
         p0
          i                 -- 3
            p0    p2
             i              -- 4
    [  0  0  1  1  2  2]    -- 5
            p0 p2          
                i           -- 6
                   i

'''

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
    Do not return anything, modify nums in-place instead.
    """
    def sortColors(self, nums: List[int]):
        n = len(nums)
        i = 0
        p0 = 0
        p2 = n - 1
        count = 1
        while True:
            if i > p2:
                break

            #lg('%d: (%d, %d, %d) -> ' % (count, i, p0, p2), end='')
            
            v = nums[i]
            if v == 2:
                swap(nums, i, p2)
                p2 -= 1
            elif v == 0:
                swap(nums, i, p0)
                p0 += 1
                i += 1
            elif v == 1:
                i += 1

            #lg('(%d, %d, %d) %s' % (i, p0, p2, nums))
            #if count == 6:
            #    br()

            count += 1











