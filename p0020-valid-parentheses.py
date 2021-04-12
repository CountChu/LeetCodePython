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
#

from typing import List
import pdb

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '{':'}', '[':']'}
        stack = []
        top_c = None
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if top_c == None:
                    return False
                elif dict[top_c] != c:
                    return False
                stack.pop()
            else:
                return False
            if len(stack) >= 1:
                top_c = stack[-1]
            else:
                top_c = None    
        return len(stack) == 0        
        



