solution_json = {
    "date": "2024/1/10",
    "design": 0,
    "coding": 26,
    "runtime": "40 ms",
    "fasterThan": "61%",
    "memory": "17.22 MB"
}

#
# https://leetcode.com/problems/sort-colors/
#
# Medium.
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
         l
         i  i
        [0, 2, 2, 1, 1, 0] 
            l  i  i  i  i
        [0, 0, 2, 1, 1, 2]    
               l
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
        for i in range(n):
            if ls[i] == 0:
                ls[i], ls[l] = ls[l], ls[i]
                l += 1
        #lg(ls)

        r = n - 1
        for i in reversed(range(l, n)):
            if ls[i] == 2:
                ls[i], ls[r] = ls[r], ls[i]
                r -= 1

        #lg(ls)






