solution_json = {
    "date": "2023/12/27",
    "design": 0,
    "coding": 14,
    "runtime": "81 ms",
    "fasterThan": "73%",
    "memory": "18.73 MB"
}

#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

         0  1  2  3  4   5
        [5, 7, 7, 8, 8, 10]
         l     m         r
                  l  m   r
'''

def bin_search(ls, n, target):
    l = 0
    r = n - 1
    while True:
        if r - l <= 1:
            if ls[r] == target:
                return r 
            if ls[l] == target:
                return l
            return -1

        m = (l + r) // 2
        #lg('(%d, %d) -> %d' % (l, r, m))

        if ls[m] == target:
            return m
        elif ls[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1

def go_right(ls, n, start_idx):
    idx = start_idx
    v0 = ls[idx]
    while True:
        if idx == n-1:
            break 

        v1 = ls[idx+1]
        if v0 != v1:
            break

        idx += 1

    return idx

def go_left(ls, n, start_idx):
    idx = start_idx
    v0 = ls[idx]
    while True:
        if idx == 0:
            break 

        v1 = ls[idx-1]
        if v0 != v1:
            break

        idx -= 1

    return idx    

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ls = nums
        n = len(ls)
        if n == 0:
            return [-1, -1]

        idx = bin_search(ls, n, target)
        if idx == -1:
            return [-1, -1]

        #br()
        r_idx = go_right(ls, n, idx)
        l_idx = go_left(ls, n, idx)
        #lg(idx, r_idx, l_idx)
        #br()

        return[l_idx, r_idx]
