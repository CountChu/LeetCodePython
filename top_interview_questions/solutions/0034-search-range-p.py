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

solution_json = {
    "date": "2022/11/7",
    "design": 0,
    "coding": 18,
    "runtime": "224 ms",
    "fasterThan": "11%",
    "memory": "15.6 MB" 
}

'''
         0  1  2  3  4  5
        [5, 7, 7, 8, 8, 10], target = 8
         i     k        j
                  i  k  j

         0  1  2  3  4  5
        [5, 7, 7, 8, 8, 10], target = 6
         i     k        j
         i  j         

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]

        i = 0 
        n = len(nums)
        j = n - 1

        found = False
        while True:
            if i > j:
                break

            k = (i + j) // 2
            if nums[k] == target:
                found = True
                break
            elif nums[k] < target:
                i = k + 1
            else:
                j = k - 1

        print('k = %d' % k)
        if found:
            i = find_left(nums, k)
            j = find_right(nums, k)
            return [i, j]
        else:
            return [-1, -1]
    
def find_left(nums, k):
    if k == 0:
        return k

    v1 = nums[k]

    while True:
        k -= 1
        v0 = nums[k]
        if v0 != v1:
            return k + 1
        
        if k == 0:
            return k

def find_right(nums, k):
    n = len(nums)
    if k == n - 1:
        return k

    v0 = nums[k]

    while True:
        k += 1
        v1 = nums[k]
        if v0 != v1:
            return k - 1

        if k == n - 1:
            return k












