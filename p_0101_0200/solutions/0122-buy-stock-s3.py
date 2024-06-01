solution_json = {
    "date": "2024/1/3",
    "design": 0,
    "coding": 10,
    "runtime": "57 ms",
    "fasterThan": "88%",
    "memory": "18.58 MB"
}

#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
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
lg = print

'''
    Input: prices = [7,1,5,3,6,4]
    Output: 7

         0  1  2  3  4  5
        [7, 1, 5, 3, 6, 4]
            b  s  b  s
               4     3      7

        [0] 7:    b = 7
        [1] 1: -, b = 1
        [2] 5: +, out = 4
        [3] 3: -, b = 3
        [4] 6: +, out = 7
        [5] 4: -, b = 4
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        ls = prices
        n = len(ls)
        v0 = ls[0]
        out = 0
        for i in range(1, n):
            v1 = ls[i]
            #lg('[%d] %d: ' % (i, v1), end='')

            if v1 > v0:
                #lg('-, ', end='')                
                out += (v1 - v0)

            v0 = v1

            #lg('out = %d' % (out))

        return out


