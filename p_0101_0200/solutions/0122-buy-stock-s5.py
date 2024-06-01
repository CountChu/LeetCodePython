solution_json = {
    "date": "2024/1/21",
    "design": 0,
    "coding": 16,
    "runtime": "66 ms",
    "fasterThan": "39%",
    "memory": "17.89 MB"
}

#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#
# Medium.
#
# You are given an integer array prices where prices[i] is the price 
# of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock. You can only hold 
# at most one share of the stock at any time. However, you can buy it 
# then immediately sell it on the same day.
#
# Find and return the maximum profit you can achieve.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
    Input: prices = [7,1,5,3,6,4]
    Output: 7

         0  1  2  3  4  5 
        [7, 1, 5, 3, 6, 4]
            b  s             5 - 1 = 4
                  b  s       6 - 3 = 3

        [0] 7:   b
        [1] 1: - b
        [2] 5: + s diff=4
        [3] 3: - b
        [4] 6: + s diff=3
        [5] 4: -

    Input: prices = [1,2,3,4,5]
    Output: 4

        [0] 1:   b
        [1] 2: + s diff=1
        [2] 3: + s diff=2 
        [3] 4: + s diff=3
        [4] 5: + s diff=4  

    Input: prices = [7,6,4,3,1]
    Output: 0

        [0] 7:   b
        [1] 6: - b
        [2] 4: - b
        [3] 3: - b
        [4] 1: - b

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        ls = prices
        n = len(ls)
        v0 = ls[0]
        b = v0
        s = None
        diff = 0
        out = 0
        for i in range(1, n):
            v0 = ls[i-1]
            v1 = ls[i]

            #lg('[%d] %d, diff = %d:' % (i, v1, diff))

            if v1 < v0:
                b = v1
                out += diff
                diff = 0
            else:
                diff = max(diff, v1 - b)

        out += diff
        
        return out
