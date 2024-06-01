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

solution_json = {
    "date": "2022/11/14",
    "design": 0,
    "coding": 0,
    "runtime": "44 ms",
    "fasterThan": "79%",
    "memory": "13.9 MB" 
}

'''
    2126                5
        2, 126          3
            1, 26       2 
                2, 6    1
                    6,  1
                26,     1     
            12, 6       1
        21, 26          2

    dp[2126] = dp[126] + dp[26]  = 3 + 2 = 5
    dp[126] = dp[26] + dp[6]     = 3
    dp[26] = dp[6] + dp['']      = 2
    dp[6] = dp['']               = 1
    dp[''] = 1

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numDecodings(self, s: str) -> int:        
        t = gen()
        #print(t)
        
        level = 0
        dp = {}
        go(t, s, level, dp)

        return dp[s]

def gen():
    t = set()
    for i in range(1, 26 + 1):
        t.add('%d' % i)

    return t

def go(t, s, level, dp):

    if len(s) == 0:
        dp[''] = 1
        return

    dp[s] = 0

    if len(s) >= 1:
        c1, s1 = split_1(s)
        if c1 in t:
            #print('%s%s, %s' % (' '*level*4, c1, s1))
            if s1 not in dp:
                go(t, s1, level+1, dp)
            dp[s] += dp[s1]

    if len(s) >= 2:
        c2, s2 = split_2(s)
        if c2 in t:
            #print('%s%s, %s' % (' '*level*4, c2, s2))
            if s2 not in dp:
                go(t, s2, level+1, dp)
            dp[s] += dp[s2]

def split_1(s):
    return s[0:1], s[1:]

def split_2(s):
    return s[0:2], s[2:]









