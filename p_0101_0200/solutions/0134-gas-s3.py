solution_json = {
    "date": "2023/12/23",
    "design": 0,
    "coding": 0,
    "runtime": "951 ms",
    "fasterThan": "99%",
    "memory": "23.3 MB"
}

#
# https://leetcode.com/problems/gas-station/
#
# There are n gas stations along a circular route, where the amount of gas 
# at the ith station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas 
# to travel from the ith station to its next (i + 1)th station. You begin 
# the journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station's 
# index if you can travel around the circuit once in the clockwise direction, 
# otherwise return -1. If there exists a solution, it is guaranteed to be unique
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''

[1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3

              0   1   2   3   4
            [ 1,  2,  3,  4,  5]
            [ 3,  4,  5,  1,  2]
             -2  -2  -2   3   3
      tank    0   0   0   3   6
      out     1   2   3

[1, 2, 3, 4, 5, 1, 8], [3, 4, 5, 1, 2, 8, 1], 6

              0   1   2   3   4   5   6
            [ 1,  2,  3,  4,  5,  1   8 ]
            [ 3,  4,  5,  1,  2,  8,  1 ]
             -2  -2  -2   3   3  -7   7  
              0   0   0   3   6   0   7

[0, 0, 0, 0, 2], [0, 0, 0, 1, 0], 4

              0   1   2   3   4
            [ 0,  0,  0,  0,  2]
            [ 0,  0,  0,  1,  0]
              0   0   0  -1   2

[0, 0, 0, 0, 2], [0, 0, 0, 0, 0], 0

              0   1   2   3   4
            [ 0,  0,  2,  0,  2]
            [ 0,  0, -2,  0,  0]
              0   0   0   0   2              

[2, 2, 2, 2, 2], [-2, -2, -2, -2, 0], 0

              0   1   2   3   4
            [ 2,  2,  2,  2,  2] 
            [-2, -2, -2, -2,  0]
              0   0   0   0   2

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        gain = []
        for i in range(n):
            gain.append(gas[i] -cost[i])
            
        if sum(gain) < 0:
            return -1

        tank = 0
        out = 0
        for i in range(n):
            tank += gain[i]
            if tank < 0:
                tank = 0
                out = i + 1

        return out








