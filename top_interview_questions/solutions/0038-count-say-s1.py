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
    "date": "2023/11/26",
    "design": 0,
    "coding": 0,
    "runtime": "53 ms",
    "fasterThan": "31%",
    "memory": "16.45 MB" 
}

'''
    countAndSay(1) = '1'
    countAndSay(2) = '11'
    countAndSay(3) = '21'
    countAndSay(4) = '1211'

    gen(1211) = 111221

         0 1 2 3
        [1 2 1 1]
    st   0 1 0 0     st: state
    ct   1 1 1 2     ct: count
                       
'''

def gen(s):

    out = ''
    st = 0
    ct = 0
    for i in range(len(s)):
        if i == 0:
            st = 0
        else:
            if s[i-1] == s[i]:
                st = 0 
            else:
                st = 1 
        #print('%s | %s' % (st, s[i]))

        if st == 0:
            ct += 1
        else:
            #print(ct, s[i])
            out += str(ct) + s[i-1]
            ct = 1 

    #print(ct, s[i])
    out += str(ct) + s[i]

    return out


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def countAndSay(self, n: int) -> str:
        ct = 1 
        out = '1'                       # 1st
        if ct == n:
            return out

        ct += 1 
        while True:
            out = gen(out)              # 2nd
            #print('out = %s' % out)
            if ct == n:
                break 

            ct += 1

        return out










