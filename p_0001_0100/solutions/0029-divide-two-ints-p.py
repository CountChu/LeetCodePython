#
# https://leetcode.com/problems/divide-two-integers/
# Given two integers dividend and divisor, divide two integers 
# without using multiplication, division, and mod operator.
# 
# The integer division should truncate toward zero, which means losing its 
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335 
# would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/6",
    "design": 0,
    "coding": 18,
    "runtime": "42 ms",
    "fasterThan": "83%",
    "memory": "14 MB" 
}

'''
    110

    3 + 3 = 6        3*2    1+1 = 2
    6 + 6 = 12       3*4    2+2 = 4
    12 + 12 = 24     3*8    4+4 = 8
    24 + 24 = 48     3*16
    48 + 48 = 96     3*32   110 - 96 = 14 
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def divide(self, dividend: int, divisor: int) -> int:
        s0 = +1
        if dividend < 0:
            s0 = -1
            dividend = -dividend

        s1 = +1
        if divisor < 0:
            s1 = -1
            divisor = -divisor

        out = 0
        while True:
            if dividend < divisor:
                break

            dividend, c = div(dividend, divisor)
            out += c
        
        out = s0 * s1 * out
        out = limit(out)
        return out

def limit(v):
    min_v = -2**31 
    if v < min_v:
        v = min_v
        return v 

    max_v = 2**31 - 1
    if v > max_v:
        v = max_v 
        return v 

    return v

def div(a, b):
    c = 1
    while True:
        if b + b > a:
            break
        
        b = b + b
        c = c + c
        #print(b, c)
    
    a -= b
    return a, c




