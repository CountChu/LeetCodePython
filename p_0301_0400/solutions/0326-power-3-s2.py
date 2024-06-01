solution_json = {
    "date": "2023/12/25",
    "design": 0,
    "coding": 4,
    "runtime": "56 ms",
    "fasterThan": "97%",
    "memory": "17.43 MB"
}

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
lg = print

'''
    27

    27 / 3 = 9
    9 / 3  = 3
    3 / 3  = 1 

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isPowerOfThree(self, n: int) -> bool:        
        if n <= 0:
            return False

        while True:
            #lg(n)
            if n == 1:
                break

            if n % 3 != 0:
                return False 

            n = n // 3

        return True



