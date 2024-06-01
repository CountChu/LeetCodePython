solution_json = {
    "date": "2024/1/8",
    "design": 0,
    "coding": 10,
    "runtime": "942 ms",
    "fasterThan": "94%",
    "memory": "23.4 MB"
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

    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3

          0  1  2  3  4
        [ 1, 2, 3, 4, 5]
        [ 3, 4, 5, 1, 2]
        
         -2 -2 -2  3  3

         [0] -2: 0 
         [1] -2: 0
         [2] -2: 0 
         [3]  3: 3
         [4]  3: 6 

    Input: gas = [2,3,4], cost = [3,4,3]
    Output: -1

          0  1  2
        [ 2, 3, 4]
        [ 3, 4, 3]

         -1 -1  1     

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = []
        for i in range(n):
            diff.append(gas[i] - cost[i])

        if sum(diff) < 0:
            return -1

        acc = 0
        out = 0
        for i in range(n):
            acc += diff[i]
            if acc < 0:
                acc = 0
                out = i + 1

            #lg('[%d] %3d: %d' % (i, diff[i], acc))

        return out








