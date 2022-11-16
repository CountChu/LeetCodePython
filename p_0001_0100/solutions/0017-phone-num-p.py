#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#
# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. 
# Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) 
# is given below. Note that 1 does not map to any letters.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/6",
    "design": 0,
    "coding": 10,
    "runtime": "78 ms",
    "fasterThan": "6%",
    "memory": "13.9 MB" 
}

'''
        0  1  2
    2: [a, b, c]

        0  1  2 
    3: [d, e, f]

    8: [t, u, v] 


'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def letterCombinations(self, digits: str) -> List[str]:
        h = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        n = len(digits)
        if n == 0:
            return []

        if n == 1:
            out = h[digits[0]]
            out = list(out)
            return out

        out = list(h[digits[0]])
        for i in range(1, n):
            out = combine(out, list(h[digits[i]]))

        return out

def combine(ls0, ls1):
    out = []
    for s0 in ls0:
        for s1 in ls1:
            out.append(s0+s1)
    return out



