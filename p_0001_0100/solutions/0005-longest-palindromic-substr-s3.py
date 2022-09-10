# 
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#       Input: s = "babad"
#       Output: "bab"
#
# Example 2:
#       Input: s = "cbbd"
#       Output: "bb"
#

from typing import List
import pdb

solution_json = {
    "date": "2022/8/28",
    "coding": 0,
    "runtime": "1023 ms",
    "fasterThan": "65%",
    "memory": "13.9 MB"
} 

class Solution:
    def find_pali_type(self, s, max_pali, i0, i1):        
        if i0 <= -1:
            return max_pali 
        if i1 >= len(s):
            return max_pali
        
        while True:
            if s[i0] == s[i1]:
                pali = s[i0:i1+1]
                #print('pali = [%s]' % pali)
                if len(max_pali) < len(pali):
                    max_pali = pali
                    #print('max_pali = [%s]' % max_pali)
                i0 -= 1 
                i1 += 1
                if i0 <= -1:
                    return max_pali 
                if i1 >= len(s):
                    return max_pali
            else:
                return max_pali

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        max_pali = ''
        for i in range(len(s)):
            if max_pali == '':
                max_pali = s[i]

            max_pali = self.find_pali_type(s, max_pali, i-1, i+1)
            max_pali = self.find_pali_type(s, max_pali, i, i+1)

        #pdb.set_trace()
        return max_pali