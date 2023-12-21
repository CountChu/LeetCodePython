solution_json = {
    "date": "2023/12/16",
    "design": 0,
    "coding": 8,
    "runtime": "1583 ms",
    "fasterThan": "12.12%",
    "memory": "16.15 MB"
}

#
# https://leetcode.com/problems/sqrtx/
#
# Given a non-negative integer x, return the square root of x rounded down to 
# the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    8
    0 * 0 = 0
    1 * 1 = 1
    2 * 2 = 4
    3 * 3 = 9
    
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def mySqrt(self, x: int) -> int:
        
        out = None
        i = 0
        while True:
            if i * i > x:
                break

            out = i 
            i += 1

        return out


