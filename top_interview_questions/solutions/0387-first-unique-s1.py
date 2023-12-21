solution_json = {
    "date": "2023/12/11",
    "design": 0,
    "coding": 0,
    "runtime": "116 ms",
    "fasterThan": "45%",
    "memory": "16.63 MB"
}

#
# https://leetcode.com/problems/first-unique-character-in-a-string/
#
# Given a string s, find the first non-repeating character in it 
# and return its index. If it does not exist, return -1.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    0 1 2 3 4 5 6 7 8 9 10 11 
    l o v e l e e t c o  d  e

    h[l] = [0, 2]
    h[o] = [1, 2]
    h[v] = [2, 1]  <---
    h[e] = [3, 3]

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        h = {}
        for i in range(n):
            c = s[i]
            if c not in h:
                h[c] = [i, 0]

            h[c][1] += 1

        #lg(h)

        for c, [i, count] in h.items():
            if count == 1:
                return i

        return -1






