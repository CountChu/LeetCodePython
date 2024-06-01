solution_json = {
    "date": "2024/1/5",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "??%",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"
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

          0   1   2   3   4
        [ 1,  2,  3,  4,  5]
        [ 3,  4,  5,  1,  2]
         -2  -2  -2   3   3
'''

def go(start, diff, n):
    acc = 0
    for i in range(n):
        j = (start + i) % n
        acc += diff[j]
        if acc < 0:
            return False 

    return True

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = []
        for i in range(n):
            diff.append(gas[i] - cost[i])
        #lg(diff)
        if sum(diff) < 0:
            return -1
        
        for i in range(n):
            if diff[i] < 0:
                continue
            if gas[i] == 0 and cost[i] == 0:
                continue

            if go(i, diff, n):
                return i

        return -1







