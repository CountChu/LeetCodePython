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
    "date": "2023/12/9",
    "design": 0,
    "coding": 0,
    "runtime": "45 ms",
    "fasterThan": "16%",
    "memory": "16.24 MB" 
}

'''
        1011 -> 8 + 2 + 1 = 11
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def hammingWeight(self, n: int) -> int:
        out = 0
        while True:
            if n == 0:
                break
            r = n % 2
            #print(r)
            if r == 1:
                out += 1
            n = n // 2

        return out
