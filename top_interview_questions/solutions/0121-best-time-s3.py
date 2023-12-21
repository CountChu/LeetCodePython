solution_json = {
    "date": "2023/12/18",
    "design": 0,
    "coding": 11,
    "runtime": "867 ms",
    "fasterThan": "54%",
    "memory": "27.45 MB"
}

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
        0 1 2 3 4 5 6 7 8
       [7 2 5 3 6 4 1 2 10]
i = 0   b
i = 1   . b
i = 2   . b .               max_p = 3
i = 3   . b . .             max_p = 3
i = 4   . b . . .           max_p = 4
i = 5   . b . . . .         max_p = 4
i = 6   . . . . . . b       max_p = 4
i = 7   . . . . . . b .     max_p = 4
i = 8   . . . . . . b . .   max_p = 9 

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        ls = prices
        n = len(ls)
        b = None
        max_p = None
        for i in range(n):
            v = prices[i]
            if b == None:
                b = v
            else:
                if v < b:
                    b = v
                else:
                    p = v - b
                    if max_p == None:
                        max_p = p 
                    else:
                        max_p = max(max_p, p)
            #lg(i, b, max_p)
        
        if max_p == None:
            return 0
        else:
            return max_p



        