solution_json = {
    "date": "2024/1/14",
    "design": 0,
    "coding": 19,
    "runtime": "42 ms",
    "fasterThan": "82%",
    "memory": "17.46 MB"
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
#lg = print

'''
    Input: n = 4
    Output: "1211"

        '1'
        '11'
        '21'
        '1211'

    Input: n = 5
        '111221'
'''

'''
    [0] 1: c=1

    [1] 1: c=2
    [2] 1: c=3
    [3] 2: c=1, 3, 1
    [4] 2: c=2  
    [5] 1: c=1  2, 2
                1, 1

    
'''

def go(s):
    n = len(s)
    if n == 1:
        return '11'

    v0 = s[0]
    c = 1
    out = ''
    for i in range(1, n):
        v1 = s[i]
        #lg('[%d] %s: c = %d, ' % (i, v1, c))
        if v1 != v0:
            #lg(c, v0)
            out += '%d%s' % (c, v0)
            c = 1
        else:
            c += 1
        v0 = v1

    #lg(v1, c)
    out += '%d%s' % (c, v1)

    #lg('')

    return out

def test():
    go('111221')
    go('111111')
    go('1111121')

    br()

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def countAndSay(self, n: int) -> str:
        #test()
        
        s = '1'
        for i in range(n-1):
            #lg('s = %s' % s)            
            s = go(s)

        return s











