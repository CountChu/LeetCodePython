solution_json = {
    "date": "2023/12/27",
    "design": 0,
    "coding": 11,
    "runtime": "50 ms",
    "fasterThan": "48%",
    "memory": "17.3 MB"
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
    Input: n = 4
    Output: "1211"

        1: ('')   -> '1'
        2: ('1')  -> '11'
        3: ('11') -> '21'
        4: ('21') -> '1211'

         0 1 2 3
        '1 2 1 1'

            v0 = 1
            count = 1

            i = 1, v0 = 1, v1 = 2, count = 1 -> '11' 
            i = 2, v0 = 2, v1 = 1, count = 1 -> '12'
            i = 3, v0 = 1, v1 = 1, count = 2

            v1 = 1, count = 2 -> '21' 

'''

def say(s):
    if s == '':
        return '1' 
    elif s == '1':
        return '11'

    n = len(s)

    v0 = s[0]
    count = 1
    out = ''
    for i in range(1, n):
        v1 = s[i]
        if v0 != v1:
            #lg(count, v0)
            out += '%d%s' % (count, v0)
            count = 1 
        else:
            count += 1
        v0 = v1

    #lg(count, v1)
    out += '%d%s' % (count, v1)

    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def countAndSay(self, n: int) -> str:
        out = ''
        for i in range(n):
            out = say(out)
            #lg('out = %s' % out)
        return out










