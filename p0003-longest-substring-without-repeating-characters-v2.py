# 
# Given a string s, find the length of the longest substring without repeating characters.
# 

from typing import List
import pdb


#
# 2021/4/10: 22 mins.  (time limit exeeded)
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        if s == '':
            return 0
        elif len(s) == 1:
            return 1
    
        hash = {}  # hash[idx] = [substr, is_end]
        max = 0
        for i, c in enumerate(s):
            hash[i] = [c, False]
            for j in range(0, i):
                #print(i, j)
                if hash[j][1] == True:
                    pass
                else:    
                    if c in hash[j][0]:
                        hash[j][1] = True

                    else:
                        hash[j][0] += c
                        
                if max < len(hash[j][0]):
                    max = len(hash[j][0])                        
                        
        #pdb.set_trace()
        return max
            