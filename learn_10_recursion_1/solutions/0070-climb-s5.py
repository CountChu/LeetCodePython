#
# https://leetcode.com/problems/climbing-stairs/
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/31",
    "design": 0,
    "coding": 0,
    "runtime": "41 ms",
    "fasterThan": "78%",
    "memory": "11.9 MB" 
}

'''
    n
    1 -> 1          -> 1
    2 -> 1+1, 2     -> 2
    3 -> 1+1+1      -> 3
         1+2 
         2+1  
    4 -> 1+1+1+1    -> 5
         1+1+2
         1+2+1
         2+1+1
         2+2
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def climbStairs(self, n: int) -> int:
        if n == 0:
            assert False
        if n == 1:
            return 1 
        if n == 2:
            return 2 

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
