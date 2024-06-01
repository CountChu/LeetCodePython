solution_json = {
    "date": "2024/1/13",
    "design": 0,
    "coding": 16,
    "runtime": "46 ms",
    "fasterThan": "65%",
    "memory": "17.68 MB"
}

#
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# Medium.
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
# You must write an a#lgorithm with O(log n) runtime complexity.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

         0  1  2  3  4  5  6
        [4, 5, 6, 7, 0, 1, 2]
         l        m        r    ls[r] < ls[l] < ls[m]   
                  l  m     r    ls[m] < ls[r] < ls[l]
                  lm r

                                ls[l] < ls[m] < ls[r]
                [3 ... 6 ... 9]

'''

def find_min_idx(ls, n):
    if n == 1:
        return 0

    l = 0
    r = n - 1
    while True:
        if r - l == 1:
            break

        m = (l + r) // 2
        #lg(l, m, r)

        if ls[r] < ls[l] < ls[m]:
            l = m
        elif ls[m] < ls[r] < ls[l]:
            r = m
        elif ls[l] < ls[m] < ls[r]:
            return l
        else:
            assert False

    if ls[l] < ls[r]:
        return l
    else:
        return r

'''
     0  1  2  3  4  5  6
    [0, 1, 2, 4, 5, 6, 7]  target = 0
     l        m        r
     l  m  r

'''

def find(ls, n, target):
    l = 0
    r = n - 1
    while True:
        if l > r:
            break

        m = (l + r) // 2
        #lg(l, m, r)

        if ls[m] == target:
            return m
        elif ls[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def search(self, nums: List[int], target: int) -> int:
        ls = nums
        n = len(ls)
        min_idx = find_min_idx(ls, n)
        #lg('min_idx = %d' % min_idx)
        
        ls = ls[min_idx:] + ls[:min_idx]
        #lg('ls = %s' % ls)
        
        idx = find(ls, n, target)
        #lg('idx = %d' % idx)
        if idx == -1:
            return -1
        
        out = (idx + min_idx) % n
        return out
