# 
# Given a string s, find the length of the longest substring without repeating characters.
# 

from typing import List
import pdb

#
# 3/28: 1 hour.
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print('s = %s' % s)
        hash = {} # c ---> str
        str_ls = []
        for i in range(len(s)):
            c = s[i]
            if c in hash:
                s1 = c+hash[c]
                if s1 not in str_ls:
                    str_ls.append(s1)
                del hash[c]
            
            found_ls = []
            for c2 in hash:
                if c in hash[c2]:
                    found_ls.append(c2)

                else:
                    hash[c2] += c
            
            for found in found_ls:
                s1 = found + hash[found]
                if s1 not in str_ls:
                    str_ls.append(s1)
                del hash[found]    

            hash[c] = ''

            print(i, c, found_ls, hash)
            
        for c in hash:
            s1 = c+hash[c]
            if s1 not in str_ls:
                str_ls.append(s1)
            
        #pdb.set_trace()    
        max_len = 0
        for s1 in str_ls:    
            if max_len < len(s1):
                max_len = len(s1)
            
        return max_len
