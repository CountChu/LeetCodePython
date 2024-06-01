#
# https://leetcode.com/problems/power-of-three/
#
# Given an integer n, return true if it is a power of three. Otherwise, return false.
#
# An integer n is a power of three, if there exists an integer x such that n == 3x.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/3",
    "design": 0,
    "coding": 6,
    "runtime": "319 ms",
    "fasterThan": "9%",
    "memory": "13.9 MB" 
}


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isPowerOfThree(self, n: int) -> bool:        
        for i in range(0, n):
            p = 3**i 
            if p == n:
                return True
            elif p > n:
                return False

        return False