solution_json = {
    "date": "2023/12/15",
    "design": 0,
    "coding": 9,
    "runtime": "44 ms",
    "fasterThan": "26%",
    "memory": "16.3 MB"
}

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
lg = print

'''
         0 1 2
        [1 2 3]
          
         0 1 2 
        [1 2 9]
             10, 1, 0
 
         0
        [9]
       1 0

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        c = 1
        for i in reversed(range(n)):
            v = digits[i] + c
            if v == 10:
                v = 0
                digits[i] = v
                c = 1 
            else:
                digits[i] = v
                c = 0

        if c == 1:
            digits.insert(0, c)

        return digits
