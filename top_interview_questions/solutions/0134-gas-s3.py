solution_json = {
    "date": "2023/12/21",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "??%",
    "memory": "?? MB"
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

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0
        
        for i in range(len(gas)):
            lg('%d: %d - %d, ' % (i, gas[i], cost[i]), end='')
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]
            lg('%d, %d' % (total_gain, curr_gain))

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1
        
        return answer if total_gain >= 0 else -1








