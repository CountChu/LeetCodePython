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

solution_json = {
    "date": "2023/12/5",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"
}

'''
                 v
           0 1 2 3 4
    gas   [1 2 3 4 5]
           7 6 5 4 8
    cost  [3 4 5 1 2]   
           4 2   3 6


          0 1 2
    gas   2 3 4
              4
    cost  3 4 3
              1

           0 1 2 3 4
    gas    4 5 3 1 4
           6 6 5 3 4
    cost.  5 4 3 4 2
           1 2 2   2 


    gas    0 0 0 2
    cost   0 0 1 0
'''

lg = print
def go(gas, cost, n, i):
    tank = gas[i]
    count = 1
    while True:
        if count == n + 1:
            break

        tank -= cost[i]
        if tank < 0:
            return False

        i1 = (i + 1) % n
        tank += gas[i1]
        #lg(count, cost[i], gas[i1], tank)
        i = i1

        count += 1
    
    return True

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canCompleteCircuit(self, gas: List[int], cost: List[int]):
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        for i in range(n):
            #lg('i = %d' % i)
            out = go(gas, cost, n, i)
            #lg('out = %s' % out)
            if out == True:
                return i

        return -1

