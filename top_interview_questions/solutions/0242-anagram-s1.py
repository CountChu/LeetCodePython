solution_json = {
    "date": "2023/12/10",
    "design": 0,
    "coding": 0,
    "runtime": "54 ms",
    "fasterThan": "58%",
    "memory": "16.84 MB"
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

'''
    s = "anagram", t = "nagaram"
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        h = {}
        for i in range(n):
            c0 = s[i]
            if c0 not in h:
                h[c0] = [0, 0]
            h[c0][0] += 1

            c1 = t[i]
            if c1 not in h:
                h[c1] = [0, 0]
            h[c1][1] += 1
        #lg(h)

        for c, [v0, v1] in h.items():
            if v0 != v1:
                return False 

        return True
