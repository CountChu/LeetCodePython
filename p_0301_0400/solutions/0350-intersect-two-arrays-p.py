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

solution_json = {
    "date": "2022/11/3",
    "design": 0,
    "coding": 0,
    "runtime": "100 ms",
    "fasterThan": "47%",
    "memory": "14.3 MB"
}

'''
    [1, 2, 2, 1] 
        1: 2
        2: 2 
    [2, 2]
        2: 2
    --->
    1: (2, 0)
    2: (2, 2)
        

    [4, 9, 5]
        4: 1
        9: 1
        5: 1
    [9, 4, 9, 8, 4]
        9: 2
        4: 2 
        8: 1        
    --->
    4: (1, 2) -> 1
    5: (1, 0)
    8: (0, 1)
    9: (1, 2) -> 1

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}                          # h[num] = [count1, count2]
        for v in nums1:
            if v not in h:
                h[v] = [0, 0]
            h[v][0] += 1

        for v in nums2:
            if v not in h:
                h[v] = [0, 0]
            h[v][1] += 1

        out = []
        for num, [count1, count2] in h.items():
            #print(num, count1, count2)
            count = min(count1, count2)
            if count == 0:
                continue

            out += [num] * count

        out.sort()
        return out





