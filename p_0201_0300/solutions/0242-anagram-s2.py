solution_json = {
    "date": "2023/12/25",
    "design": 0,
    "coding": 5,
    "runtime": "41 ms",
    "fasterThan": "94.97%",
    "memory": "17.96 MB"
}

#
# https://leetcode.com/problems/valid-anagram/
#
# Given two strings s and t, return true if t is an anagram of s, 
# and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of 
# a different word or phrase, typically using all the original letters 
# exactly once.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

def build_set(s):
    h = {}
    for c in s:
        if c not in h:
            h[c] = 0
        h[c] += 1

    out = set()
    for c, count in h.items():
        out.add(c*count)
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isAnagram(self, s: str, t: str) -> bool:
        set0 = build_set(s)
        set1 = build_set(t)
        return set0 == set1
