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
    "runtime": "81 ms",
    "fasterThan": "5%",
    "memory": "14.1 MB" 
}

'''
    2126               5
        2, 126         3 
            1, 26      2              
                2, 6   1   
            12, 6      1
        21, 26         2


    dp[6] = 1
    dp[26] = 1 + dp[6] = 2
    dp[126] = dp[26] + dp[6] = 3
    dp[2126] = dp[126] + dp[26] = 3 + 2 = 5

    dp[27] = 0 + dp[7] = 1
    dp[10] = 1 + 0 = 0

    dp[06] = xxx


    2101              1
        2, 101        1
            1, 01     0 
            10, 1     1
        21, 01        0
           
    dp[2101] = dp[101] + dp[01] = 1
    dp[101] = dp[01] + dp[1] = 1
    dp[01] = 0
    dp[1] = 1

    1201234
        1, 201234
            2, 01234            0  <---
                0, 1234         3
                    1, 234      2
                        2, 34   1
                        23, 4   1
                    12, 34      1
                01, 234         2
                    2, 34       1 
                    23, 4       1
            20, 1234
        12, 01234

    123123
        1, 23123                6
            2, 3123             3
                3, 123          3
                    1, 23       2
                        2, 3    1
                    12, 3       1
                31, 23          0   <---
                    2, 3        1
            23, 123             3
                1, 23
                    2, 3
                12, 3
        12, 3123                3
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numDecodings(self, s: str) -> int:        
        table = gen()
        level = 0
        dp = {}
        go(table, s, level, dp)
        return dp[s]

def go(table, s, level, dp):

    if len(s) == 0:
        return

    elif len(s) == 1:
        #print('%s%s' % (' '* level* 4, s))
        if s in table:
            dp[s] = 1
        else:
            dp[s] = 0

    elif len(s) == 2:
        code, next_s = split_1(s)
        #print('%s%s, %s' % (' '* level* 4, code, next_s))

        dp[s] = 0

        if code not in table:
            dp[s] = 0

        if code in table and next_s in table:
            dp[s] = 1

        if s in table:
            dp[s] += 1

    elif len(s) >= 3:
        exit = True

        code1, s1 = split_1(s)
        #print('%s%s, %s' % (' '* level* 4, code1, s1))

        if s1 not in dp:
            go(table, s1, level+1, dp)

        code2, s2 = split_2(s)
        #print('%s%s, %s' % (' '* level* 4, code2, s2))

        if s2 not in dp:  
            go(table, s2, level+1, dp)

        dp[s] = 0

        if code1 in table:
            dp[s] += dp[s[1:]]

        if code2 in table:
            dp[s] +=  dp[s[2:]]

    #print('%s%s' % (' '* level* 4, dp))


def split_1(s):
    code = s[0:1]
    next_s = s[1:]
    return code, next_s

def split_2(s):
    code = s[0:2]
    next_s = s[2:]
    return code, next_s

def gen():
    table = set()
    for i in range(1, 26+1):
        table.add('%d' % i)

    return table
