solution_json = {
    "date": "2023/12/13",
    "design": 0,
    "coding": 0,
    "runtime": "88 ms",
    "fasterThan": "30%",
    "memory": "17.93 MB"
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
           0 1 2 3 4 5 6 7 8
    nums: [1 2 3 3 3 3 4 5 9]   target: 3
           l       m       r

           0 1 2 3 4  5
    nums: [5 7 7 8 8 10]   target: 8 
           l   m      r
               l m    r

    nums: [1]   target: 1
           lr

    nums: [2 2]  target: 2
           l r

           0 1 2
    nums: [1 2 3]  target: 1
           l m r
           l r

'''

def find(nums, target):
    l = 0
    r = len(nums) - 1

    if l == r:
        if nums[l] == target:
            return l 
        else:
            return -1
    
    while True:
        #lg(l, r)
        if r - l == 1:
            if nums[r] == target:
                return r

            if nums[l] == target:
                return l 
            break

        m = (r + l) // 2 
        #lg(m)
        if nums[m] == target:
            return m 

        elif nums[m] < target <= nums[r]:
            l = m 

        elif nums[l] <= target < nums[m]:
            r = m

        else:
            return -1

    return -1

'''
           0 1 2 3 4 5 6 7 8
    nums: [1 2 3 3 3 3 4 5 9]   target: 3
           l   m   r 
           l m r
               .
'''

def find_left(nums, r, target):
    l = 0
    while True:
        #lg(l, r)
        if r - l <= 1:
            if nums[l] == target:
                return l 

            if nums[r] == target:
                return r
            
            break

        m = (r + l) // 2
        #lg(m)

        if nums[m] == target:
            r = m 
        else:
            l = m

    return r

'''
           0 1 2 3 4 5 6 7 8
    nums: [1 2 3 3 3 3 4 5 9]   target: 3
                   l   m   r
                   l m r 

           0 1 2
    nums: [3 3 3]  target 3
             l r

'''

def find_right(nums, l, target):
    r = len(nums) - 1
    while True:
        #lg(l, r)
        if r - l <= 1:
            if nums[r] == target:
                return r

            if nums[l] == target:
                return l 
            
            break

        m = (r + l) // 2
        #lg(m)

        if nums[m] == target:
            l = m
        else:
            r = m

    return l

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        m = find(nums, target)
        #lg('m = %d' % m)

        if m == -1:
            return [-1, -1]


        l = find_left(nums, m, target)
        #lg('l = %d' % l)

        r = find_right(nums, m, target)
        #lg('r = %d' % r)

        return [l, r]








