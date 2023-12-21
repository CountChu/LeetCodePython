solution_json = {
    "date": "2023/12/20",
    "design": 0,
    "coding": 23,
    "runtime": "61 ms",
    "fasterThan": "77%",
    "memory": "17.92 MB"
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

Case 1:

     0 1 2 3 4 5
    [7 1 5 3 6 4]
       b s         4
           b s     3  

         0  1  2  3  4  5
        [7  1  5  3  6  4]
    i=0  b
    i=1     b
    i=2     b  s
    i=3           b
    i=4           b  s
    i=5                 .    


Case 2:

     0 1 2 3 4
    [1 2 3 4 5]
     b       s     4

         0 1 2 3 4
        [1 2 3 4 5]
    i=0  b
    i=1    s
    i=2      s
    i=3        s
    i=4          s



Case 3:

     0 1 2 3 4
    [7 6 4 3 1]    0
  
         0 1 2 3 4
        [7 6 4 3 1]    0
    i=0  b
    i=1    b
    i=2      b
    i=3        b
    i=4          b

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:

        ls = prices
        n = len(ls)
        b = -1
        s = -1
        out = 0
        for i in range(n):
            #lg('%d: ' % i, end='')
            v = ls[i]
            if i == 0:
                b = ls[i]
            else:
                if s > v:
                    out += s - b
                    b = v
                    s = -1

                else:
                    if b > v:
                        b = v
                    elif b < v:
                        s = ls[i]

            #lg('%d, %d, ' % (b, s))

        if s != -1:
            out += s - b

        return out
