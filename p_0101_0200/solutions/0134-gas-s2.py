solution_json = {
    "date": "2023/12/21",
    "design": 0,
    "coding": 20,
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
             0  1  2  3  4
    gas:    [1, 2, 3, 4, 5]
    cost:   [3, 4, 5, 1, 2]
                      4
                         4-1+5=8
             8-2+1=7
                7-3+2=6
                   6-4+3=5
                      5-5=0
                 
             0  1  2  3  4
    gas:    [0, 0, 0, 0, 2]
    cost:   [0, 0, 0, 1, 0]

'''

def go(gas, cost, n, start):
    idx0 = start
    tank = gas[start]
    lg('%d: %d, tank = %d' % (start, gas[start], tank))
    
    for i in range(1, n):
        idx1 = (start + i) % n
        tank -= cost[idx0]
        lg('%d: %d, %d, tank = %d' % (idx1, cost[idx0], gas[idx1], tank))
        if tank < 0:
            return False
        tank += gas[idx1]
        idx0 = idx1

    tank -= cost[idx0]
    lg('%d: %d, tank = %d' % (start, cost[idx0], tank))
    if tank < 0:
        return False
    else:
        return True

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            if go(gas, cost, n, i):
                return i

        return -1







