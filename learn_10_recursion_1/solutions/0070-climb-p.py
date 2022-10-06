#
# https://leetcode.com/problems/climbing-stairs/
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
#
# Example 1:
#       Input: n = 2
#       Output: 2
#
# Example 2: 
#       Input: n = 3
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
    "runtime": "62 ms",
    "fasterThan": "17%",
    "memory": "13.9 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        i = 3 
        while True:
            if i > n:
                break

            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        
        return dp[n]

