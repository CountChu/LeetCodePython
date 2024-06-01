solution_json = {
    "date": "2024/1/20",
    "design": 0,
    "coding": 19,
    "runtime": "49 ms",
    "fasterThan": "9%",
    "memory": "16.42 MB"
}

#
# https://leetcode.com/problems/decode-ways/
#
# Medium.
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
#lg = print

'''
    codes = ['1', '2', ..., '26']

    Input: s = "226"
    Output: 3

        (226)
            check 226           dp[226] = dp[26] + dp[6]
            2, (26)
                check 26        dp[26] = 1 + dp[6] = 2
                2, (6)
                    check 6     dp[6] = 1
            22, (6)
                check 6         dp[6] = 1
'''

def gen_codes():
    out = set()
    base = 1
    for i in range(26):
        code = i + base
        out.add('%d' % code)
    return out

def go(s, level, codes, dp):
    #lg('%s%s' % ('    '*level, s))
    
    dp[s] = 0    
    if s in codes:
        #lg('%s+1' % ('    '*level))
        dp[s] = 1

    for i in range(len(s)):
        s0 = s[:i]
        s1 = s[i:] 
        if s0 in codes:
            if not s1 in dp:
                go(s1, level+1, codes, dp)
            dp[s] += dp[s1]

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numDecodings(self, s: str) -> int:    
        level = 0
        codes = gen_codes()
        #lg(codes)
        dp = {}
        go(s, level, codes, dp)
        return dp[s]




