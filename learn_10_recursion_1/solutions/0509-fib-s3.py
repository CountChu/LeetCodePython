#
# https://leetcode.com/problems/fibonacci-number/
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, 
# called the Fibonacci sequence, such that each number is the sum 
# of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#
# Given n, calculate F(n).
#
# Example 1:
#       Input: n = 2
#       Output: 1
#
# Example 2: 
#       Input: n = 3
#       Output: 2
# 
# Example 3:
#       Input: n = 4
#       Output: 3
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "59 ms",
    "fasterThan": "47%",
    "memory": "13.9 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def fib(self, n: int) -> int:
        dp = {}                         # dp[n]= f(n)
        dp[0] = 0 
        dp[1] = 1
        out = f(n, dp)
        br()
        return out

def f(n, dp):
    if n in dp:
        return dp[n]

    dp[n] = f(n - 1, dp) + f(n - 2, dp) 
    return dp[n]

