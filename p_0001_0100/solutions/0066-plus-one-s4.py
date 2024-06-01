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
    "date": "2023/11/28",
    "design": 0,
    "coding": 0,
    "runtime": "45 ms",
    "fasterThan": "20%",
    "memory": "16.39 MB" 
}

'''
    0  1  2
   [1  2  9] 
          
       1  0 
    0  3
    1

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        c = 1
        out = []
        for i in reversed(range(n)):
            v = digits[i]
            v += c
            if v >= 10:
                v -= 10 
                c = 1
            else:
                c = 0 
            out.append(v)
            #print(v)

        if c == 1:
            out.append(c)

        n = len(out)
        out1 = []
        for i in reversed(range(n)):
            out1.append(out[i])
        
        return out1