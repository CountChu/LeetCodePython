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

solution_json = {
    "date": "2022/11/2",
    "design": 0,
    "coding": 2,
    "runtime": "47 ms",
    "fasterThan": "74%",
    "memory": "13.9 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def hammingWeight(self, n: int) -> int:
        out = 0
        while True:
            if n == 0:
                break

            b = n % 2 
            if b == 1:
                out += 1

            n = n // 2

        return out
