solution_json = {
    "date": "2024/1/8",
    "design": 0,
    "coding": 14,
    "runtime": "53 ms",
    "fasterThan": "34.13%",
    "memory": "17.33 MB"
}

#
# https://leetcode.com/problems/count-and-say/
#
# Medium
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

        '1'

        '11'

        '21'

        '1211'

        '111221'

                    
            [0] 1: c0 = None, c1 = 1, count = 1
            [1] 1: c0 = 1,    c1 = 1, count = 2
            [2] 1: c0 = 1,    c1 = 1, count = 3 
            [3] 2: c0 = 1,    c1 = 2, count = 1  -> (3, '1')
            [4] 2: c0 = 2,    c1 = 2, count = 2 
            [5] 1: c0 = 2,    c1 = 1, count = 1  -> (2, '2')
                                                 -> (1, '1')



'''

def say(s):
    n = len(s)
    c0 = None
    count = 0
    out = ''
    for i in range(n):
        c1 = s[i]
        if c0 != None and c0 != c1:
            #lg(count, c0)
            out += '%d%s' % (count, c0)
            count = 0
        count += 1
        c0 = c1
    #lg(count, c0)
    out += '%d%s' % (count, c0)
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(n - 1):
            s = say(s)
        return s












