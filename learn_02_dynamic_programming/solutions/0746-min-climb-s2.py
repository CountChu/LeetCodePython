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
# Constraints:
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/30",
    "design": 0,
    "coding": 0,
    "runtime": "51 ms",
    "fasterThan": "99%",
    "memory": "14.1 MB" 
}

'''
      0   1   2
    [10, 15, 20]
      v   v            25
      v       v        30
          v   v        35
          v      v     15 <--- 

    dp[0] = 10
    dp[1] = 15
    dp[2] = 20 + min(dp[1], dp[0]) = 30
    dp[3] =  0 + min(dp[2], dp[1]) 15
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        
        for i in range(len(dp)):
            if i < n:
                dp[i] = cost[i]

            if i  >= 2:
                dp[i] += min(dp[i-1], dp[i-2])

        return dp[-1]
