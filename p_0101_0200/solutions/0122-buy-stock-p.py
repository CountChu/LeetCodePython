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

solution_json = {
    "date": "2022/11/14",
    "design": 0,
    "coding": 0,
    "runtime": "140 ms",
    "fasterThan": "40%",
    "memory": "15.2 MB" 
}

'''
    [7, 1, 5, 3, 6, 4]
        b  s            -> 4
              b  s      -> 3

     p  v  p  v  p  v

    [5, 7, 2, 7, 3, 3, 5, 3, 0]
     v  p  v  p  v  v  p  -  v 
        2     5        2

    [5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]
     p  v  p  v  p  p  v  p  -  v  p  v  p  v
           1     4        7        7     1

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        trend = find_trend(prices)
        #print(trend)
        
        find_v = False
        profit = 0
        out = 0
        for t, p in zip(trend, prices):
            if t == 'v':
                find_v = True 
                profit = 0
                profit -= p

            if t == 'p' and find_v:
                profit += p
                out += profit
                find_v = False

            #print(t, p, profit, out)

        return out


def find_trend(prices):
    n = len(prices)
    trend = ['-'] * n

    for i, p1 in enumerate(prices):
        if i == 0:
            p2 = prices[i + 1]
            if p1 > p2:
                trend[i] = 'p'
            elif p1 < p2:
                trend[i] = 'v'
        elif i == n - 1:
            p0 = prices[i - 1]
            if p0 > p1:
                trend[i] = 'v'
            elif p0 < p1:
                trend[i] = 'p'
        else:
            p0 = prices[i - 1]
            p2 = prices[i + 1]
            if p0 < p1 and p1 > p2:
                trend[i] = 'p'
            elif p0 == p1 and p1 > p2:
                trend[i] = 'p'
            elif p0 < p1 and p1 == p2:
                trend[i] = 'p'
            elif p0 > p1 and p1 < p2:
                trend[i] = 'v'
            elif p0 == p1 and p1 < p2:
                trend[i] = 'v'
            elif p0 > p1 and p1 == p2:
                trend[i] = 'v'                

    return trend




