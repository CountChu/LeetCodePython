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
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"
}

'''
    [7, 1, 5, 3, 6, 4]
        v        v

    [7, 6, 4, 3, 1]
     v           v

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        for i in range(1, len(prices)):
            d = get_max_diff(prices, i)
            #print(i, d)
            out = max(d, out)

        return out

def get_max_diff(prices, idx):
    out = 0
    p1 = prices[idx]
    for i in range(0, idx):
        p0 = prices[i]
        d = p1 - p0
        if d > 0:
            out = max(d, out)

    return out
