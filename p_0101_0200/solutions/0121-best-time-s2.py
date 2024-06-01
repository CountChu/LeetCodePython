#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# You are given an array prices where prices[i] is the price of a given stock 
# on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
            0  1  2  3  4  5  6  7  8
           [7  2  5  3  6  4  1  2 10]  
    i = 0   7
    i = 1      2  
    i = 2      2  3 
    i = 3      2  3  . 
    i = 4      2        4 
 
'''

solution_json = {
    "date": "2023/12/2",
    "design": 0,
    "coding": 0,
    "runtime": "889 ms",
    "fasterThan": "30%",
    "memory": "27.33 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        buy = None 
        out = 0
        for i, price in enumerate(prices):
            if buy == None:
                buy = price
            else:
                buy = min(buy, price)
            profit = price - buy 
            out = max(out, profit)
            #lg(i, price, buy, profit, out)

        return out






