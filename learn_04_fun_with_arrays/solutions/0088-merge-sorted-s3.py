#
# https://leetcode.com/problems/merge-sorted-array/
#
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, 
# but instead be stored inside the array nums1. To accommodate this, 
# nums1 has a length of m + n, where the first m elements denote the elements 
# that should be merged, and the last n elements are set to 0 and should be ignored. 
# nums2 has a length of n.
#
# Example 1:
#       Input:
#           nums1 = [1,2,3,0,0,0], 
#           m = 3, 
#           nums2 = [2,5,6], 
#           n = 3
#       Output: [1,2,2,3,5,6]
#
# Example 2: 
#       Input:
#           nums1 = [1], 
#           m = 1, 
#           nums2 = [], 
#           n = 0
#       Output: [1]
#
# Example 3: 
#       Input:
#           nums1 = [0], 
#           m = 0, 
#           nums2 = [1], 
#           n = 1
#       Output: [1]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/1",
    "design": 0,
    "coding": 0,
    "runtime": "69 ms",
    "fasterThan": "41%",
    "memory": "14 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    '''
        nums1, m, i 
        nums2, n, j
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        out = []
        i = 0
        j = 0 
        while True:
            if i == m and j == n:
                break
            elif i < m and j < n:
                if nums1[i] <= nums2[j]:
                    out.append(nums1[i])
                    i += 1
                else:
                    out.append(nums2[j])
                    j += 1
            elif i < m and j == n:
                out.append(nums1[i])
                i += 1 
            elif i == m and j < n:
                out.append(nums2[j])
                j += 1
            else:
                assert False

        for i in range(len(nums1)):
            nums1[i] = out[i]


