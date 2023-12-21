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

solution_json = {
    "date": "2023/12/4",
    "design": 0,
    "coding": 0,
    "runtime": "65 ms",
    "fasterThan": "52%",
    "memory": "17.82 MB" 
}

'''
    i: buy
    j: sell


     0 1 2 3 4 5
    [7 1 5 3 6 4]
       b s b s
         4   3      7
     i j
       i j .        4 
         i j 
           i j .    3

     0 1 2 3 4
    [1 2 3 4 5]
     b       s      
             4      4
     i j . . .

'''


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        p = prices
        n = len(p)

        out = 0
        i = 0
        j = 1
        while True:
            if j == n:
                break

            #lg(i, j)
            if p[i] > p[j]:
                i += 1 
                j += 1
            else:
                if j == n - 1:
                    #lg('b: %d' % p[i])
                    #lg('s: %d' % p[j])
                    out += p[j] - p[i]
                    break

                else:
                    if p[j] > p[j+1]:
                        #lg('b: %d' % p[i])
                        #lg('s: %d' % p[j])
                        out += p[j] - p[i]
                        i = j 
                        j = j + 1
                    else:
                        j += 1

        return out