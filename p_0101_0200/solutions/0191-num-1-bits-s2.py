solution_json = {
    "date": "2023/12/24",
    "design": 0,
    "coding": 3,
    "runtime": "38 ms",
    "fasterThan": "64%",
    "memory": "17.26 MB"
}

#
# https://leetcode.com/problems/number-of-1-bits/
#
# Write a function that takes an unsigned integer and returns the number 
# of '1' bits it has (also known as the Hamming weight).
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: n = 00000000000000000000000000001011
    Output: 3

    00000000000000000000000000001011
                                   1
                                  1
                                 1  
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def hammingWeight(self, n: int) -> int:
        mask = 1
        out = 0
        for i in range(32):
            if (mask & n) != 0:
                out += 1
            mask = mask << 1
        return out
