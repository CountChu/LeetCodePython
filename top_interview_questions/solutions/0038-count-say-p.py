#
# https://leetcode.com/problems/count-and-say/
#
# The count-and-say sequence is a sequence of digit strings defined by 
# the recursive formula:
#
#       countAndSay(1) = "1"
#
#       countAndSay(n) is the way you would "say" the digit string from 
#       countAndSay(n-1), which is then converted into a different digit string.
#
# To determine how you "say" a digit string, split it into the minimal number 
# of substrings such that each substring contains exactly one unique digit. 
# Then for each substring, say the number of digits, then say the digit. 
# Finally, concatenate every said digit.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/8",
    "design": 0,
    "coding": 13,
    "runtime": "100 ms",
    "fasterThan": "37%",
    "memory": "14.2 MB" 
}

'''
        n = 1 -> '1'
        n = 2 -> '1'   -> one 1 -> '11'
        n = 3 -> '11'  -> two 1 -> '21'
        n = 4 -> '21'  -> one 2 one 1 -> 1211
        n = 5 -> '1211' -> one 1 one 2 two 1 -> 111221
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def countAndSay(self, n: int) -> str:
        out = '1'
        if n == 1:
            return out

        for i in range(2, n+1):
            ls = split(out)
            out = combine(ls)
        
        return out

def split(s):
    ls = []
    pre_c = None
    s1 = ''
    for c in s:
        if pre_c != None:
            if pre_c != c:
                ls.append(s1)
                s1 = ''
        s1 += c
        pre_c = c

    if s1 != '':
        ls.append(s1)
 
    return ls

def combine(ls):
    out = ''
    for s in ls:
        out += ('%d' % len(s)) + s[0]

    return out 











