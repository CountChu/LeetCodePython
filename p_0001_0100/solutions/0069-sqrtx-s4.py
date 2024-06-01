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

solution_json = {
    "date": "2023/11/29",
    "design": 0,
    "coding": 0,
    "runtime": "1323 ms",
    "fasterThan": "15%",
    "memory": "16.1 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def mySqrt(self, x: int) -> int:
        out = 0
        for i in range(1, x+1):
            if i * i > x:
                break

            out = i        

        return out
