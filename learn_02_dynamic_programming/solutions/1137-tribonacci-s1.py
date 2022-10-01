#
# https://leetcode.com/problems/n-th-tribonacci-number/
#
# The Tribonacci sequence Tn is defined as follows: 
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
# Example 1:
#       Input: n = 4
#       Output: 4
#
# Example 2: 
#       Input: n = 25
#       Output: 1389537
# 
# Constraints:
#       0 <= n <= 37
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/8",
    "again": ["2022/9/30"],
    "design": 0,
    "coding": 0,
    "runtime": "55 ms",
    "fasterThan": "25%",
    "memory": "13.8 MB" 
}

'''
    T0 = 0
    T1 = 1
    T2 = 1
    T3 = 0 + 1 + 1 = 2 
    T4 = 1 + 1 + 2 = 4
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n+1)
        if n == 0:
            return dp[0] 

        dp[1] = 1
        if n == 1:
            return dp[1]

        dp[2] = 1
        if n == 2:
            return dp[2]

        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1] 

        return dp[-1]
