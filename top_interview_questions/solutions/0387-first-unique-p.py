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

solution_json = {
    "date": "2022/11/3",
    "design": 0,
    "coding": 11,
    "runtime": "214 ms",
    "fasterThan": "60%",
    "memory": "14.1 MB" 
}

'''
    0  1  2  3  4  5  6  7
    l, e, e, t, c, o, d, e
    T

    l -> 0
    e -> 1
    e -> None
    t -> 3 
    c -> 4
    o -> 5
    d -> 6
    e -> None
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i, c in enumerate(s):
            if c not in h:
                h[c] = i
            else:
                h[c] = None

        min_v = None
        for c, idx in h.items():
            if idx == None:
                continue

            if min_v == None:
                min_v = idx
            else:
                min_v = min(min_v, idx)

        if min_v == None:
            out = -1
        else:
            out = min_v

        return out





