solution_json = {
    "date": "2023/12/18",
    "design": 0,
    "coding": 28,
    "runtime": "38 ms",
    "fasterThan": "70%",
    "memory": "16.48 MB"
}

#
# https://leetcode.com/problems/decode-ways/
#
# A message containing letters from A-Z can be encoded into numbers 
# using the following mapping:
#
#       'A' -> "1"
#       'B' -> "2"
#       ...
#       'Z' -> "26"
# 
# To decode an encoded message, all the digits must be grouped then mapped back 
# into letters using the reverse of the mapping above (there may be multiple ways). 
# For example, "11106" can be mapped into:
#
#       "AAJF" with the grouping (1 1 10 6)
#       "KJF" with the grouping (11 10 6)
#
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped 
# into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
#
# The test cases are generated so that the answer fits in a 32-bit integer.
#


from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print


'''
      0 1 2 3
    ' 2 1 2 6'

    (0, '2126')                       = 5
        '2', '126' -> (1, '126')      = 3
            '1', '26' -> (2, '26')    = 2
                '2', '6' -> (3, '6')  = 1
                    '6', ''           = 1              
                '26', ''              = 1
            '12', '6' -> (2, '6')     = 1            
        '21', '26' -> (2, '26')       = 2

'''

def gen_num_s():
    out = set()
    for i in range(1, 26+1):
        out.add('%s' % i)
    return out

def go(i, s, num_s, dp):
    #lg(i, s[i:])

    n = len(s)
    if i == n:
        return 1

    out = 0
    if i <= n - 1:
        if s[i] in num_s:
            if i + 1 not in dp:
                dp[i+1] = go(i+1, s, num_s, dp)
            out += dp[i+1]

    if i <= n - 2:
        if s[i:i+2] in num_s:
            if i + 2 not in dp:
                dp[i+2] = go(i+2, s, num_s, dp)
            out += dp[i+2]
    
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numDecodings(self, s: str) -> int:
        num_s = gen_num_s()
        #lg(num_s)
        dp = {}
        out = go(0, s, num_s, dp)
        return out
