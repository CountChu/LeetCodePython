#
# Given a string s, return the longest palindromic substring in s.
#

from typing import List
import pdb

solution_json = {
    "date": "2021/3/29",
    "bug": "Time Limit Exceeded"
}

class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        def is_palindromic(s):
            s2 = ''
            for i in reversed(range(len(s))):
                s2 += s[i]
            return s == s2    
    
        print('s = %s' % s)
        table = []
        pali_ls = []
        for i in range(len(s)):
            c = s[i]
            for j in range(len(table)):
                table[j] += c
            table.append(c)
            
            start_idx = -1
            for j in range(len(table)):
                row = table[j]
                if is_palindromic(row):
                    start_idx = j
                    break
               
            '''   
            for j in reversed(range(start_idx + 1, len(table))):
                del table[j]
            '''
               
            for row in table:
                if is_palindromic(row):
                    if row not in pali_ls:
                        pali_ls.append(row)
                print(row)
            print('----', start_idx)    
            
        max_s = ''    
        max_len = 0    
        for s in pali_ls:
            if len(s) > max_len:
                max_len = len(s)
                max_s = s
            
        return max_s        
