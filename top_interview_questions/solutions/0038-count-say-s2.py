solution_json = {
    "date": "2023/12/14",
    "design": 0,
    "coding": 12,
    "runtime": "50 ms",
    "fasterThan": "49%",
    "memory": "16.29 MB"
}

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
lg = print

'''
    1 
    1 1
    2 1
    1 2 1 1
'''

'''
       0 1 2 3
    s: 1 2 1 1

       0 1
    s: 1 1
'''

def say(s):
    if s == '':
        return '1'

    if s == '1':
        return '11'

    n = len(s)
    c0 = s[0]
    count = 1
    out = ''
    for i in range(1, n):
        c1 = s[i]
        if c0 == c1:
            count += 1
        else:
            out += '%d%s' % (count, c0)
            #lg(count, c0, out)
            count = 1
        c0 = c1

    out += '%d%s' % (count, c1)
    #lg(count, c1, out)

    return out


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def countAndSay(self, n: int) -> str:
        out = ''
        for i in range(n):
            out = say(out)
            #lg(out)
        
        return out











