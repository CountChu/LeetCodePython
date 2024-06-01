solution_json = {
    "date": "2024/1/11",
    "design": 0,
    "coding": 30,
    "runtime": "43 ms",
    "fasterThan": "26%",
    "memory": "17.28 MB"
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
    Input: s = "226"
    Output: 3
                            
        (226)               dp['226'] = 3
            2, (26)         dp['226'] = 2
                26     ->   dp['26'] = 2
                2, (6)      dp['26'] = 1
                    6  ->   dp['6'] = 1
            22, (6)         dp['226'] = 1
                6      ->   dp['6'] = 1
'''

def gen_codes():
    out = set()
    for i in range(1, 27):
        out.add('%d' % i)

    return out

def go(codes, s, level, dp):
    #lg('%s%s' % ('    '*level, s))

    if s not in dp:
        dp[s] = 0

    if len(s) <= 2:
        if s in codes:
            #lg('%sGot it' % ('    '*level))
            dp[s] = 1

    if len(s) >= 2:
        s0 = s[0:1]
        s1 = s[1:]
        #lg('%s%s, %s'  % ('    '*level, s0, s1))
        if s0 in codes:
            if not s1 in dp:
                go(codes, s1, level+1, dp)
            dp[s] += dp[s1]

    if len(s) >= 3:
        s0 = s[0:2]
        s1 = s[2:]
        #lg('%s%s, %s'  % ('    '*level, s0, s1))    
        if s0 in codes:
            if not s1 in dp:            
                go(codes, s1, level+1, dp)
            dp[s] += dp[s1]

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numDecodings(self, s: str) -> int:        
        codes = gen_codes()
        level = 0
        dp = {}
        go(codes, s, level, dp)
        return dp[s]



