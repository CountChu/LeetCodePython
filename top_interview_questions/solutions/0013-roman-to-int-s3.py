solution_json = {
    "date": "2023/12/13",
    "design": 0,
    "coding": 13,
    "runtime": "48 ms",
    "fasterThan": "74%",
    "memory": "16 MB"
}

#
# https://leetcode.com/problems/roman-to-integer/
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
    I: 1
    V: 5
    X: 10
    L: 50
    C: 100
    D: 500
    M: 1000
    IV: 4
    IX: 9
    XL: 40
    XC: 90
    CD: 400
    CM: 900

    0 1 2 3 4 5 6
    M C M X C I V
    . 1000
      . . 900 
          . . 90
              . . 4
'''

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

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def romanToInt(self, s: str) -> int:
        n = len(s)
        idx = 0
        out = 0
        while True:
            c2 = s[idx:idx+2]
            if c2 in h:
                #lg('c2 = %s' % c2)
                out += h[c2]
                idx += 2
            else:
                c1 = s[idx:idx+1]
                #lg('c1 = %s' % c1)
                out += h[c1]
                idx += 1

            if idx >= n:
                break

        return out
