#
# https://leetcode.com/problems/daily-temperatures/
#
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days 
# you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/21",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"
}

''' 
      0   1   2   3   4   5   6   7
    [73, 74, 75, 71, 69, 72, 76, 73], 
    [ 1,  1,  4,  2,  1,  1,  0,  0]
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n
        for i in range(0, n-1):
            t0 = temperatures[i]
            count = 0
            found = False
            for j in range(i, n):
                t1 = temperatures[j]
                if t0 < t1: 
                    found = True
                    break
                count += 1
            if found:
                out[i] = count
        
        return out

