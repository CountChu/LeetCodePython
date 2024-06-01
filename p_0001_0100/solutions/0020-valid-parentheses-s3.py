#
# https://leetcode.com/problems/valid-parentheses/
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
#
# Constraints:
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/20",
    "design": 0,
    "coding": 0,
    "runtime": "62 ms",
    "fasterThan": "32%",
    "memory": "13.9 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isValid(self, s: str) -> bool:
        h = {
            ']': '[',
            '}': '{',
            ')': '(',
        }
        stack = []
        for i in range(len(s)):
            if s[i] not in h:
                stack.append(s[i])
            else:
                if stack == []:
                    return False

                top = stack.pop()
                if h[s[i]] != top:
                    return False 

        if stack != []:
            return False

        return True
