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
    "date": "2022/10/30",
    "design": 0,
    "coding": 0,
    "runtime": "38 ms",
    "fasterThan": "81%",
    "memory": "13 MB" 
}

'''
     0  1  2  3  4
    [0, 1, 1, 2, 4]

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2 
    dp[3] = dp[0] + dp[1] + dp[2]
    dp[4] = dp[1] + dp[2] + dp[3]

'''
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        dp = [0] * (n + 1)

        dp[0] = 0    
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
        return dp[-1]

