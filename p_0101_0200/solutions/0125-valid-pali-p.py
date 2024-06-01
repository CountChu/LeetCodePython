#
# https://leetcode.com/problems/valid-palindrome/
#
# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters 
# include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/31",
    "design": 0,
    "coding": 8,
    "runtime": "144 ms",
    "fasterThan": "12%",
    "memory": "14.3 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isPalindrome(self, s: str) -> bool:
        s = convert(s)
        #rint(s)
        out = is_pali(s)
        return out

def convert(s):
    out = ''
    for i in range(len(s)):
        if s[i].isalpha():
            out += s[i].lower()

        elif s[i].isdigit():        
            out += s[i]

    return out

def is_pali(s):
    n = len(s)
    i = 0
    j = n - 1
    while True:
        if i > j:
            break

        if s[i] != s[j]:
            return False

        i += 1 
        j -= 1

    return True

