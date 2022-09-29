#
# https://leetcode.com/problems/min-cost-climbing-stairs/
#
# You are given an integer array cost where cost[i] is the cost of ith step 
# on a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
# Example 1:
#       Input: cost = [10,15,20]
#       Output: 15
#
# Example 2: 
#       Input: cost = [1,100,1,1,1,100,1,1,100,1]
#       Output: 6
#
# Constraints:
#       2 <= cost.length <= 1000
#       0 <= cost[i] <= 999
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/8",
    "again": ["2022/9/29"],
    "design": 0,
    "coding": 0,
    "runtime": "117 ms",
    "fasterThan": "19%",
    "memory": "14.1 MB" 
}

'''
     0    1  2  3  4    5  6  7    8  9
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

n = 2
     0    1   2
    [1, 100]
          V   V
     V        V
    dp[2] = min(c[1], c[0])

n = 3
     0    1  2   3
    [1, 100, 1]
             V   V
          V      V
    dp[3] = min(c[2]+dp[2], c[1]+dp[1])

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        assert n >= 2, n

        dp = [0] * (n + 1) 

        for i in range(2, n + 1):
            case1 = cost[i-1] + dp[i-1]
            case2 = cost[i-2] + dp[i-2]
            dp[i] = min(case1, case2)
            #print(i, case1, case2, dp)

        return dp[-1]











