solution_json = {
    "date": "2024/1/8",
    "design": 0,
    "coding": 16,
    "runtime": "46 ms",
    "fasterThan": "68%",
    "memory": "17.88 MB"
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
         l        m        r
                  l  m     r
                  l  mr

 
    test_solution(sln, [1, 3, 5], 0, -1)

         0  1  2 
        [1, 3, 5]
         l  m  r




'''

def find_min(ls, n):
    l = 0
    r = n - 1
    while True:
        m = (l + r) // 2

        if m == r or m == l:
            break

        if ls[r] < ls[l] < ls[m]:
            l = m

        elif ls[m] < ls[r] < ls[l]:
            r = m

        elif ls[l] < ls[m] < ls[r]:
            r = m

        else:
            assert False

    if ls[l] < ls[r]:
        return l
    else:
        return r

'''
    [1, 3], 3

         0  1
        [1, 3]
         lm r
'''

def bin_search(ls, n, t):
    l = 0
    r = n - 1
    pre_m = None
    while True:
        m = (l + r) // 2
        #lg(l, m, r)

        if pre_m != None:
            if pre_m == m:
                break

        if ls[m] == t:
            return m
        
        elif ls[m] < t:
            l = m

        else:
            r = m

        pre_m = m

    if ls[l] == t:
        return l
    elif ls[r] == t:
        return r

    return -1 

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def search(self, nums: List[int], target: int) -> int:
        ls = nums
        n = len(ls)
        idx = find_min(ls, n)
        #lg('idx = %d' % idx)
        ls = ls[idx:] + ls[:idx]
        #lg('ls = %s' % ls)
        out = bin_search(ls, n, target)
        if out == -1:
            return -1

        out = (out + idx) % n
        return out
     
