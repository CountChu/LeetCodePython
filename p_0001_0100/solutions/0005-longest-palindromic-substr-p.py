# 
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string s, return the longest palindromic substring in s.
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/17",
    "design": 0,    
    "coding": 0,
    "runtime": "959 ms",
    "fasterThan": "75%",    
    "memory": "14 MB"
} 

'''
        0 1 2 3 4
        b a b a d
    0   i
    1     i
    2       i        

        0 1 2 3
        c b b d
        i
          i
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) 
        out = ''
        for i in range(n):

            j, k = find_longest(s, n, i, i)
            pali = s[j:k+1]
            #print(i, j, k, pali)
            if len(out) < len(pali):
                out = pali

            if i + 1 < n and s[i] == s[i+1]:
                j, k = find_longest(s, n, i, i+1)
                pali = s[j:k+1]
                #print(i, j, k, pali)
                if len(out) < len(pali):
                    out = pali

        return out

def find_longest(s, n, i, j):
    out = None
    while True:
        if i < 0:
            break

        if j >= n:
            break

        if s[i] == s[j]:
            out = (i, j)
        else:
            break

        i -= 1
        j += 1

    return out    


