#
# https://leetcode.com/problems/powx-n/
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
# Example 1:
#       Input: x = 2.00000, n = 10
#       Output: 1024.00000
#
# Example 2: 
#       Input: x = 2.10000, n = 3
#       Output: 9.26100
# Example 3:
#       Input: x = 2.00000, n = -2
#       Output: 0.25000
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "55 ms",
    "fasterThan": "45%",
    "memory": "14 MB" 
}

'''
    1.1 ^ 30
    x ^ 30
    1, 2, 4, 8, 16 -> 14
    1, 2, 4, 8     -> 6
    1, 2, 4        -> 2
    1, 2           -> 0

    
    x ^ 10
    1, 2, 4, 8    -> 2
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n = -n 
            x = 1/x

        out = 1 
        while True:
            x2, t = f(x, n)
            out = x2 * out
            #print(out, x2, t)   
            n = n - t     
            if n == 0:
                break
        return out

def f(x, n):
    t = 1
    out = x
    while True:
        #print(t)
        if t * 2 > n:
            break
        t = t * 2
        out = out * out
    return out, t

