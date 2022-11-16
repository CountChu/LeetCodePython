# 
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string s, return the longest palindromic substring in s.
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/4",
    "design": 0,    
    "coding": 20,
    "runtime": "?? ms",
    "fasterThan": "",    
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"
} 

'''
        0 1 2 3 4
        b a b a d
      0 b a b
      1   a b a
      2     b
      3       a
      4         d  
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:

        out = ''
        for i in range(len(s)):
            pali = get_pali(s, i)
            #print(i, pali)
            if len(out) < len(pali):
                out = pali            
        
        return out

def get_pali(s, i):
    j = len(s) - 1
    out = ''
    while True:
        if i > j:
            break

        if not is_pali(s, i, j):
            j -= 1
        else:
            pali = s[i:j+1]
            if len(out) < len(pali):
                out = pali
            break

    return out

def is_pali(s, i, j):
    while True:
        if i >= j:
            break

        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True

