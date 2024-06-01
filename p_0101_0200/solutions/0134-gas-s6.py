solution_json = {
    "date": "2024/1/13",
    "design": 0,
    "coding": 30,
    "runtime": "946 ms",
    "fasterThan": "88%",
    "memory": "23.33 MB"
}

#
# https://leetcode.com/problems/gas-station/
#
# Medium.
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
                       V
           0   1   2   3   4
        [  1,  2,  3,  4,  5]
        [  3,  4,  5,  1,  2]
          -2  -2  -2   3   3    sum = 0

                          out = -1
        [0] -2: acc = -2
        [1] -2: acc = -2
        [2] -2: acc = -2
        [3]  3: acc = 6,  out = 3
        [4]  3: acc = 12


    Input: gas = [2,3,4], cost = [3,4,3]
    Output: -1

           0   1   2
        [  2,  3,  4]
        [  3,  4,  3]
          -1  -1   1     sun = -1

    Case 3:

          0  1   2  3  4
        [-2, 2, -3, 3, 3]  sum >= 0 
    
        [0] -2: acc = 0
        [1]  2: acc = 2, out = 1
        [2] -3: acc = 0
        [3]  3: acc = 0, out = 3 
        [4]  3: acc = 3  


'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff_ls = []
        for i in range(n):
            diff_ls.append(gas[i] - cost[i])
        #lg(diff_ls)
        if sum(diff_ls) < 0:
            return -1

        acc0 = 0
        acc = 0
        out = -1
        for i in range(n):
            diff = diff_ls[i]
            acc += diff
            if acc < 0:
                out = -1                
                acc = diff
            
            if acc >= 0:
                if out == -1 and acc0 <= 0:
                    out = i

            #lg('[%d] %3d: acc = %3d, out = %3d' % (i, diff, acc, out))
            acc0 = acc

        return out






