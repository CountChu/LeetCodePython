solution_json = {
    "date": "2023/12/13",
    "design": 0,
    "coding": 6,
    "runtime": "44 ms",
    "fasterThan": "40%",
    "memory": "16.48 MB"
}

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
lg = print

'''
         j j
         0 1 2 3 4 5
    s0   f l o w e r
    s1   f l o w
    s2   f l i g h t
    out  f l

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        h = len(strs)
        w = len(strs[0])
        for i in range(1, len(strs)):
            w = min(w, len(strs[i]))
        #lg(h, w)
        
        out = ''
        same = True
        for j in range(w):
            if not same:
                break

            s0 = strs[0]
            for i in range(1, h):
                s1 = strs[i]
                if s0[j] != s1[j]:
                    same = False
                    break

            if same:
                out += s0[j]

        return out

