#
# https://leetcode.com/problems/n-th-tribonacci-number/
#
# The Tribonacci sequence Tn is defined as follows: 
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
# 
# Constraints:
#       0 <= n <= 37
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def tribonacci(self, n: int) -> int:
        return 4