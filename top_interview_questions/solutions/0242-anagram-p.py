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

solution_json = {
    "date": "2022/11/3",
    "design": 0,
    "coding": 4,
    "runtime": "53 ms",
    "fasterThan": "91%",
    "memory": "14.4 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h_s = build_hash(s)
        h_t = build_hash(t)
        
        return h_s == h_t

def build_hash(s):
    h = {}
    for i, c in enumerate(s):
        if c not in h:
            h[c] = 0
        h[c] += 1

    return h