solution_json = {
    "date": "2024/1/11",
    "design": 0,
    "coding": 15,
    "runtime": "62 ms",
    "fasterThan": "66%",
    "memory": "18.86 MB"
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

        [0] 7:  
        [1] 1: b
        [2] 5: diff = 4
        [3] 3: b
        [4] 6: diff = 3
        [5] 4: b

    test_solution(sln, [1, 2, 3, 4, 5], 4)        

        [0] 1:
        [1] 2:
        [2] 3:
        [3] 4:
        [4] 5:


'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        ls = prices
        n = len(ls)

        v0 = ls[0]
        diff = 0
        out = 0
        buy = v0
        for i in range(1, n):
            v1 = ls[i]
            #lg('[%d] %d:' % (i, v1))
            if v0 > v1:
                #lg('diff = %d' % diff)
                buy = v1
                #lg('buy = %d' % buy)
                out += diff
                diff = 0
            else:
                diff = max(diff, v1 - buy)
            v0 = v1

        out += diff
        
        
        return out
