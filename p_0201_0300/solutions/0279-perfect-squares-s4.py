#
# https://leetcode.com/problems/perfect-squares/
#
# Given an integer n, return the least number of perfect square numbers that sum to n.
#
# A perfect square is an integer that is the square of an integer; 
# in other words, it is the product of some integer with itself. 
# For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/17",
    "design": 0,
    "coding": 0,
    "runtime": "5523 ms",
    "fasterThan": "27",
    "memory": "14.7 MB" 
}

'''
    1, 2, 3,  4,  5,  6,  7,  8,  9
    1, 4, 9, 16, 25, 36, 49, 64, 81 

    dp[1]: 1
    dp[2]: dp[1] + 1 = 2
    dp[3]: dp[2] + dp[1] = 3
    dp[4]: 1
    dp[5]: dp[4] + 1 = 2
    dp[6]: dp[4] + dp[2] = 3
    dp[7]: dp[4] + dp[3] = 4
    dp[8]: dp[4] + dp[4] = 2
    dp[9]: 1
    dp[10]: dp[9] + 1 = 2
    dp[11]: dp[9] + dp[2] = 3

    dp[12]: dp[9] + dp[3]  = 1 + 3 = 4
            dp[4] + dp[8]  = 1 + 2 = 3
            dp[1] + dp[11] = 1 + 3 = 4 
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numSquares(self, n: int) -> int:
        sqr_set = set()
        for i in range(1, n+1):
            sqr = i*i 
            if sqr > n:
                break 
            sqr_set.add(sqr)

        dp = {}
        for i in range(1, n+1):
            build(i, sqr_set, dp)

        #print(dp)
        return dp[n]

def build(x, sqr_set, dp):
    if x in sqr_set:
        dp[x] = 1
    else:
        min_num = None
        for x1 in sqr_set:
            if x1 >= x:
                continue 

            x2 = x - x1
            num = dp[x1] + dp[x2]
            if min_num == None:
                min_num = num 
            elif min_num > num:
                min_num = num

        dp[x] = min_num













