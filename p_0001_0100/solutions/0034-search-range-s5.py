solution_json = {
    "date": "2024/1/14",
    "design": 0,
    "coding": 25,
    "runtime": "78 ms",
    "fasterThan": "77.89%",
    "memory": "19.01 MB"
}

#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an a#lgorithm with O(log n) runtime complexity.
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
         l     m         r
                  l  m   r
'''

def find(ls, target):
    #lg('find')

    n = len(ls)
    l = 0
    r = n - 1
    while True:
        m = (l + r) // 2
        #lg(l, m, r)

        if l > r:
            break

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
                 r0
     l     m     r
              l  r

     0  1  2  3  4  5  6
    [5, 7, 7, 8, 8, 8, 8]
                       r0
     l        m        r
     l  m     r
           l  r

     0  1
    [2, 2]
     r0 
     l

'''

def find_left(ls, r0):
    #lg('find_left')
    target = ls[r0]
    l = 0
    r = r0
    while True:
        m = (l + r) // 2
        #lg(l, m, r)

        if r - l <= 1:
            break

        if ls[m] == target:
            r = m
        else:
            l = m + 1

    if ls[l] == target:
        return l
    else:
        return r

'''
     0  1  2  3  4   5
    [5, 7, 7, 8, 8, 10]
             l0
              l  m   r
                 r

'''

def find_right(ls, l0):
    #lg('find_right')
    target = ls[l0]
    l = l0
    r = len(ls) - 1
    while True:
        m = (l + r) // 2
        #lg(l, m, r)

        if r - l <= 1:
            break

        if ls[m] == target:
            l = m
        else:
            r = m - 1

    if ls[r] == target:
        return r
    else:
        return l


def test():
    
    ls = [5, 7, 7, 8, 8, 10]

    idx = find(ls, target=8)
    assert idx == 4, idx

    idx = find(ls, target=5)
    assert idx == 0, idx

    idx = find(ls, target=0)
    assert idx == -1, idx

    idx = find_left(ls, r0=4)
    assert idx == 3, idx

    ls = [5, 7, 7, 8, 8, 8, 8]

    idx = find_left(ls, r0=3)
    assert idx == 3, idx

    idx = find_left(ls, r0=4)
    assert idx == 3, idx

    idx = find_left(ls, r0=5)
    assert idx == 3, idx    

    idx = find_left(ls, r0=6)
    assert idx == 3, idx

    ls = [5, 7, 7, 8, 8, 10]

    idx = find_right(ls, l0=3)
    assert idx == 4, idx

    ls = [5, 7, 7, 8, 8, 8, 8, 10]    
 
    idx = find_right(ls, l0=3)
    assert idx == 6, idx    

    idx = find_right(ls, l0=4)
    assert idx == 6, idx    

    idx = find_right(ls, l0=5)
    assert idx == 6, idx    

    idx = find_right(ls, l0=6)
    assert idx == 6, idx    

    ls = [2, 2]

    idx = find(ls, 2)
    assert idx == 0, idx

    idx = find_right(ls, 0)
    assert idx == 1, idx

    idx = find_left(ls, 0)
    assert idx == 0, idx

    #br()

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #test()
        
        ls = nums
        n = len(nums)
        if n == 1:
            if ls[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        idx = find(ls, target)
        if idx == -1:
            return [-1, -1]

        l = find_left(ls, idx)
        r = find_right(ls, idx)
        return [l, r]

