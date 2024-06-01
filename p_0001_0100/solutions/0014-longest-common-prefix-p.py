#
# https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/22",
    "design": 0,
    "coding": 0,
    "runtime": "37 ms",
    "fasterThan": "82%",
    "memory": "16.34 MB" 
}

'''
    strs[0]
        0 1 2 3 4 5
        f l o w e r

    strs[1]
        0 1 2 3
        f l o w 

    strs[2]
        0 1 2 3 4 5
        f l i g h t

    s = strs[0]
    s = common(s, strs[1])
    s = common(s, strs[2])
    s = common(s, strs[3])
'''

def common(s0, s1):
    n = min(len(s0), len(s1))
    out = ''
    for i in range(n):
        if s0[i] != s1[i]:
            break 

        out += s0[i]

    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        for i in range(1, len(strs)):
            s = common(s, strs[i])
            if s == '':
                return ''

        return s

