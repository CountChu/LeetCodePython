# 
# https://leetcode.com/problems/regular-expression-matching/
#
# Given an input string (s) and a pattern (p), 
# implement regular expression matching with support for '.' and '*' where: 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Example 1:
#       Input: s = "aa", p = "a"
#       Output: false
#
# Example 2:
#       Input: s = "aa", p = "a*"
#       Output: true
#
# Example 3:
#       Input: s = "ab", p = ".*"
#       Output: true
#

from typing import List
import sys 
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isMatch(self, s: str, p: str) -> bool:   
        return False 
