solution_json = {
    "date": "2023/12/11",
    "design": 0,
    "coding": 0,
    "runtime": "52 ms",
    "fasterThan": "63%",
    "memory": "16.72 MB"
}

#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
#
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays 
# and you may return the result in any order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    ls1 [4 9 5]
    ls2 [9 4 9 8 4]
    h[4] = [1, 1]
    h[5] = [1, 0]
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls1 = nums1 
        ls2 = nums2 
        
        h = {}

        for v in ls1:
            if v not in h:
                h[v] = [0, 0]

            h[v][0] += 1

        for v in ls2:
            if v not in h:
                h[v] = [0, 0]

            h[v][1] += 1
        
        out = []
        for v, [c0, c1] in h.items():
            d = min(c0, c1)
            if d >= 1:
                out += [v] * d

        return out

