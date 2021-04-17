# 
# Given a string s, return the longest palindromic substring in s.
#

from typing import List
import pdb

#
# 4/11: 1 hour, Runtime: 3376 ms, Memory: 15.8 MB
#

class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        def expand_pali(s, pali, idx0, idx1):

            while True:
                
                if idx0 == -1:
                    break
                if idx1 == len(s):
                    break

                if s[idx0] == s[idx1]:
                    pali = s[idx0] + pali + s[idx1]
                    idx0 -= 1
                    idx1 += 1
                else:
                    break

            return pali
    
        def find_pali(s, idx):
            pali = s[idx]
            idx0 = idx - 1
            idx1 = idx + 1
            
            pali_ls = []
            
            pali1 = expand_pali(s, pali, idx0, idx1)
            pali_ls.append(pali1)
            
            if idx+1 < len(s) and s[idx] == s[idx+1]:
                pali = s[idx] + s[idx+1]
                idx0 = idx - 1
                idx1 = idx + 2
            
                pali2 = expand_pali(s, pali, idx0, idx1)
                pali_ls.append(pali2)
            
            return pali_ls
                    
    
        hash = {} # hash[c] = [idx1, idx2]
        n = len(s)
        lognest_pali = ''
        for i in range(n):
            c = s[i]
            pali_ls = find_pali(s, i)
            if len(lognest_pali) < len(pali_ls[0]):
                lognest_pali = pali_ls[0]
            if len(pali_ls) == 2:
                if len(lognest_pali) < len(pali_ls[1]):
                    lognest_pali = pali_ls[1]
           
            #print(i, c, pali_ls)
        
        return lognest_pali