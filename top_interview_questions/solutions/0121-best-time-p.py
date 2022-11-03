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

solution_json = {
    "date": "2022/10/31",
    "design": 0,
    "coding": 0,
    "runtime": "2522 ms",
    "fasterThan": "42%",
    "memory": "25.1 MB" 
}

'''
     v  v  v  v  v  v
     0  1  2  3  4  5
    [7, 1, 5, 3, 6, 4]
       -  +  -  +  - 
       0  1  2  3  4

     v           v
     0  1  2  3  4
    [7, 6, 4, 3, 1]
      -   -  -  - 
     
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for v in prices:
            if min_price > v:
                min_price = v 

            profit = v - min_price
            if profit > 0:
                if profit > max_profit:
                    max_profit = profit

            #print(v, min_price, max_profit)

        return max_profit
