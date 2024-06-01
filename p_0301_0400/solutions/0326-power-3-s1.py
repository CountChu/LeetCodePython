solution_json = {
    "date": "2023/12/10",
    "design": 0,
    "coding": 0,
    "runtime": "65 ms",
    "fasterThan": "88%",
    "memory": "16.4 MB"
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
    3^0 = 1
    3^1 = 3
    3^2 = 9
    3^3 = 27
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isPowerOfThree(self, n: int) -> bool:       
        v = 1
        while True:
            if v == n:
                return True 

            if v > n:
                return False

            v = 3 * v

