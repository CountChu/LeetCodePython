solution_json = {
    "date": "2023/12/27",
    "design": 0,
    "coding": 40,
    "runtime": "50 ms",
    "fasterThan": "40%",
    "memory": "17.53 MB"
}

#
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated 
# at an unknown pivot index k (1 <= k < nums.length) such that the resulting 
# array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 
# and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

         0  1  2  3  4  5  6
        [4, 5, 6, 7, 0, 1, 2]
                     t

        [0, 1, 2, 4, 5, 6, 7]
         l        m        r
         l  m  r

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

         0  1  2  3  4  5  6
        [4, 5, 6, 7, 0, 1, 2]
                     .  start_idx = 4

         0  1  2  3  4  5  6
        [0, 1, 2, 4, 5, 6, 7]
         l        m        r 
         l  m  r


     0  1
    [1, 3], 0
     l  r

'''

def trans_ls(ls, n):
    if n == 1:
        return ls, 0

    min_idx = 0
    for i in range(1, n):
        v0 = ls[i-1]
        v1 = ls[i]
        if v0 > v1:
            min_idx = i
    #lg(min_idx)
    return ls[min_idx:] + ls[:min_idx], min_idx

def bin_search(ls, n, target):
    l = 0
    r = n - 1
    while True:
        m = (l + r) // 2
        #lg('(%d, %d) -> %d, ' % (l, r, m))

        if r - l <= 1:
            if ls[r] == target:
                return r

            if ls[l] == target:
                return l

            return -1

        if ls[m] == target:
            return m
        elif ls[m] > target:
            r = m - 1
        else:
            l = m + 1 

    return -1

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def search(self, nums: List[int], target: int) -> int:
        ls = nums
        n = len(ls)
        ls, min_idx = trans_ls(ls, n)
        idx = bin_search(ls, n, target)
        if idx == -1:
            return -1

        out = (idx + min_idx) % n
        return out
     
