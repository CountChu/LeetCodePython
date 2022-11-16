# 
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string s, return the longest palindromic substring in s.
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/5",
    "design": 0,    
    "coding": 0,
    "runtime": "2369 ms",
    "fasterThan": "32%",    
    "memory": "13.9 MB"
} 

'''    
        0 1 2 3 4
        b a b a d
          .

        0 1 2 3
        c b b d
          . .

        0 1 2 3 4 5 6 7 8 9 10
        a a c a b d k a c a a
    0   a a 
        a
                b         

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ''
        i = 0
        while True:
            if i >= len(s):
                break

            if i + 1 < len(s) and s[i] == s[i+1]:
                pali = longest_pali(s, i, i+1)
                #print(i, pali)
                if len(out) < len(pali):
                    out = pali

            pali = longest_pali(s, i, i)
            #print(i, pali)
            if len(out) < len(pali):
                out = pali

            i += 1

        return out

def longest_pali(s, i, j):
    out = s[i:j+1]
    i -= 1
    j += 1
    while True:
        if i <= -1:
            break
        if j >= len(s):
            break

        if s[i] == s[j]:
            out = s[i:j+1]
            #print(i, j, out)
        else:
            break

        i -= 1
        j += 1

    return out


