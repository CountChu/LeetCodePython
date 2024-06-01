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
    "date": "2022/10/16",
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
        dp = {}                         # dp[num] = (ls, len(ls))
        sqr_set = set()
        for i in range(1, n + 1):
            #print(i)
            sqr = i * i
            if sqr <= n:
                sqr_set.add(sqr)
                dp[sqr] = ([sqr], 1)

            if i not in sqr_set:
                build(i, dp)

        out = dp[n][1]
        #br()
        return out

def build(n, dp):
    #print('n = %d --------' % n)
    found_ls = None

    pair_set = set()    
    for num, (sql_ls, ls_len) in dp.items():
        n1 = n - num
        if n1 <= 0:
            break

        if (num, n1) in pair_set or (n1, num) in pair_set:
            continue

        #print('pair = (%d, %d), sql_ls = %s' % (num, n1, sql_ls))
        pair_set.add((num, n1))

        #ls = dp[num] + dp[n1]
        #print('ls = %s' % ls)
        if found_ls == None:
            found_ls = dp[num][0] + dp[n1][0] 
        
        elif dp[num][1] + dp[n1][1] < len(found_ls):
            found_ls = dp[num][0] + dp[n1][0]    

        if found_ls != None and len(found_ls) == 2:      
            break  

    #print('pair_set = %s' % pair_set)
    #print('found_ls = %s' % found_ls)
    #assert n not in dp
    dp[n] = (found_ls, len(found_ls))

    return












