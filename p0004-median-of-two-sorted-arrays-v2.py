# 
# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
# 

from typing import List
import pdb

#
# 4/10: 12 mins, Runtime: 104 ms, Memory 14.6MB
#

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls = []
        i = 0
        j = 0
        
        while True:
            if i == len(nums1) and j == len(nums2):
                break
            elif i == len(nums1):
                v2 = nums2[j]
                ls.append(v2)
                j += 1
            elif j == len(nums2):
                v1 = nums1[i]
                ls.append(v1)
                i += 1
            else:    
                v1 = nums1[i]
                v2 = nums2[j]
                if v1 < v2:
                    ls.append(v1)
                    i += 1
                else:
                    ls.append(v2)
                    j += 1
        
        idx = len(ls) // 2
        if len(ls) % 2 == 1:
            m = ls[idx]
        else:
            m = (ls[idx-1] + ls[idx]) / 2.0

        return m