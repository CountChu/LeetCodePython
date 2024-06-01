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
    "date": "2022/10/15",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded" 
}

'''
Case 1:
    12 = 4 + 4 + 4
    1, 4, 9

Case 2:
    13 = 4 + 9
    1, 4, 9

    13 = 9 + 4
       = 4 + 9
       = 1 + 12
    12 = 9 + 3
       = 4 + 8
       = 1 + 11 
     3 = 1 + 2
     2 = 1 + 1
     8 = 4 + 4
       = 1 + 7
     4 = 1 + 3
     7 = 4 + 3
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numSquares(self, n: int) -> int:
        dp = {}
        sqr_ls = []
        for i in range(1, n + 1):
            #print(i)
            sqr = i * i
            if sqr <= n:
                sqr_ls.append(sqr)
                dp[sqr] = [sqr]

            if i not in sqr_ls:
                build(i, dp)

        out = len(dp[n])
        return out

def build(n, dp):
    #print('n = %d' % n)
    found_ls = None
    for num, sql_ls in dp.items():
        n1 = n - num
        if n1 <= 0:
            break

        #print('n1 = %d' % n1)
        if n1 in dp:
            ls = dp[num] + dp[n1]
            #print('ls = %s' % ls)
            if found_ls == None:
                found_ls = ls 
            elif len(ls) < len(found_ls):
                found_ls = ls            

    #print(found_ls)
    assert n not in dp
    dp[n] = found_ls

    return












