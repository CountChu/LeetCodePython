#
# https://leetcode.com/problems/plus-one/
#
# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. The digits are ordered 
# from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/31",
    "design": 0,
    "coding": 0,
    "runtime": "74 ms",
    "fasterThan": "8%",
    "memory": "13.9 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        out = []
        for v in reversed(digits):
            c, v = adder(v, c)
            #print(c, v)
            out.append(v)
        
        if c == 1:
            out.append(c)

        out.reverse()
        return out

def adder(v, c):
    v += c
    if v == 10:
        return 1, 0 
    else:
        return 0, v