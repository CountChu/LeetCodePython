solution_json = {
    "date": "2024/5/27",
    "design": 0,
    "coding": 16,
    "runtime": "49 ms",
    "fasterThan": "42%",
    "memory": "16 MB"
}

#
# https://leetcode.com/problems/roman-to-integer/
#
# Easy.
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two ones added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
# which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:
#
#       I can be placed before V (5) and X (10) to make 4 and 9. 
#       X can be placed before L (50) and C (100) to make 40 and 90. 
#       C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer.
#

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    II, 2

    XII, 12

    XXVII, 27,   
        X+X+V+I+I 

    IV, 4
        V - I = 5 - 1 = 4

    IX, 9
        X - I = 10 - 1 = 9

    XL, 40 
    XC, 90
    CD, 400
    CM, 900

    MCMXCIV, 1994

        M, CM, XC, IV
        1000, 900, 90, 4
'''

lg = print
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def romanToInt(self, s: str) -> int:
        h = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

        out = 0
        i = 0
        while True:
            s1 = s[i:i+1]
            s2 = s[i:i+2]
            if s2 in h:
                #lg(s2)
                out += h[s2]
                i += 2
            elif s1 in h:
                #lg(s1)
                out += h[s1]
                i += 1
            else:
                assert False, 's1: %s, s2:%s' % (s1, s2)

            if i >= len(s):
                break

        return out
