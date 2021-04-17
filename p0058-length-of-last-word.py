# 
# Given a string s consists of some words separated by spaces, 
# return the length of the last word in the string. 
# If the last word does not exist, return 0.
# 
# A word is a maximal substring consisting of non-space characters only.
# 

from typing import List
import pdb

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        pre_count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                count = 0
            else:
                count += 1
                pre_count = count
            line = ''
            line += 's[%d] = %s, ' % (i, s[i])
            line += 'count = %d, pre_count = %d' % (count, pre_count)
            print(line)
        return pre_count
        
