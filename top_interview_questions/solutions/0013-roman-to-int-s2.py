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

import pdb
br = pdb.set_trace


solution_json = {
    "date": "2021/4/11",
    "again": ["2022/10/31"],
    "coding": 7,
    "runtime": "91 ms",
    "fasterThan": "58%",    
    "memory": "13.9 MB"
}

'''
    0 1 2 3 4 5 6
    M C M X C I V

    M,    CM,  XC, IV
    1000, 900, 90, 4    ---> 1994   

    IV: 4
    IX: 9
    XL: 40
    XC: 90
    CD: 400
    CM: 900
'''

class Solution:

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
        idx = 0
        while True:
            cc = s[idx:idx+2]

            if cc not in h:
                out += h[cc[0]]
                idx += 1
            else:
                out += h[cc]
                idx += 2

            if idx >= len(s):
                break

        return out
