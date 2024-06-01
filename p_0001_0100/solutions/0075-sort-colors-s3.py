solution_json = {
    "date": "2023/12/31",
    "design": 0,
    "coding": 20,
    "runtime": "36 ms",
    "fasterThan": "82%",
    "memory": "17.33 MB"
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
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

         0  1  2  3  4  5
        [2, 0, 2, 1, 1, 0]
         l              r
         i
        [0, 0, 2, 1, 1, 2]
         li          r
            li       r
            l  i     r 
        [0, 0, 1, 1, 2, 2]
            l  i  r

    Input: nums = [2,0,1]
    Output: [0,1,2]

         0  1  2
        [2, 0, 1]
         l     r
         i    
        [1, 0, 2] 
         l  r
         i  i
        [0, 1, 2] 
            lr
            i

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
    Do not return anything, modify nums in-place instead.
    """
    def sortColors(self, nums: List[int]) -> None:
        ls = nums
        n = len(ls)
        l = 0
        i = 0
        r = n - 1
        while True:
            #lg('[%d], %d, %d, %s' % (i, l, r, ls))

            if ls[i] == 2:
                ls[i], ls[r] = ls[r], ls[i]
                r -= 1
            elif ls[i] == 1:
                i += 1
            elif ls[i] == 0:

                ls[i], ls[l] = ls[l], ls[i]
                l += 1
                i += 1

            if i > r:
                break



