solution_json = {
    "date": "2024/1/13",
    "design": 0,
    "coding": 0,
    "runtime": "82 ms",
    "fasterThan": "60%",
    "memory": "18.8 MB"
}

#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an a##lgorithm with O(log n) runtime complexity.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

         0  1  2  3  4   5
        [5, 7, 7, 8, 8, 10]
                  v  v
 
'''

'''
    Case 1:

         0  1  2  3  4   5
        [5, 7, 7, 8, 8, 10]     target = 8
         l     m         r
                  l  m   r

'''
def find(ls, target):
    n = len(ls)
    l = 0
    r = n - 1
    while True:
        if l > r:
            break

        m = (l + r) // 2

        if ls[m] == target:
            return m
        elif ls[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1

'''
     0  1  2  3  4   5
    [5, 7, 7, 8, 8, 10]     
                 r0         target = ls[r0]
     l     m     r          ls[m] != target
              l  r          r - l == 1          


     0  1  2  3  4  5  6  7  8
    [5, 7, 7, 8, 8, 8, 8, 8, 8]  
                             r0
     l           m           r
              r

     0  1  2  3  4  5  6  7  8
    [5, 7, 7, 8, 8, 8, 8, 8, 8] 
                    r0
     l        m     r
              r         

     0  1
    [2, 2]
     r0      
'''

def find_left(ls, r0):
    l = 0
    r = r0
    target = ls[r0]
    while True:
        m = (l + r) // 2
        #lg(l, m, r)

        if r - l <= 1:
            break

        if ls[m] != target:
            l = m + 1
        else:
            r = m

    if ls[l] == target:
        return l
    else:
        return r

'''
     0  1  2  3  4   5   6   7   8
    [5, 7, 7, 8, 8, 10, 11, 12, 13]
                 l0  
                 l       m       r
                 l   r 

'''

def find_right(ls, l0):
    n = len(ls)
    l = l0
    r = n - 1
    target = ls[l0]    
    while True:
        m = (l + r) // 2
        #lg(l, m, r)

        if r - l <= 1:
            break

        if ls[m] != target:
            r = m - 1
        else:
            l = m

    if ls[r] == target:
        return r 
    else:
        return l

def test():
    ls = [5, 7, 7, 8, 8, 10]
    idx = find(ls, 8)
    assert idx == 4, idx

    left_idx = find_left(ls, idx)
    assert left_idx == 3
    #lg('left_idx = %d' % left_idx)

    ls = [5, 7, 7, 8, 8, 8, 8, 8, 8] 

    if True:
        left_idx = find_left(ls, 3)
        assert left_idx == 3

    if True:
        left_idx = find_left(ls, 4)
        assert left_idx == 3
    
    if True:    
        left_idx = find_left(ls, 5)
        assert left_idx == 3
    
    if True:        
        left_idx = find_left(ls, 6)
        assert left_idx == 3
    
    if True:
        left_idx = find_left(ls, 7)
        assert left_idx == 3
    
    if True:
        left_idx = find_left(ls, 8)
        assert left_idx == 3        
    
    if True:
        left_idx = find_left(ls, 8)
        assert left_idx == 3

    if True:
        ls = [5, 7, 7, 8, 8, 10, 11, 12, 13]
        right_idx = find_right(ls, 4)
        assert right_idx == 4, right_idx

    if True:
        right_idx = find_right(ls, 3)
        assert right_idx == 4, right_idx

    br()


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ls = nums
        if len(ls) == 1:
            if ls[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        idx = find(ls, target)
        #lg('idx = %d' % idx)
        if idx == -1:
            return [-1, -1]

        left_idx = find_left(ls, idx)
        #lg('left_idx = %d' % left_idx)

        right_idx = find_right(ls, idx)
        #lg('right_idx = %d' % right_idx)

        return [left_idx, right_idx]

