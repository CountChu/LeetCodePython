from typing import List
import pdb

#
# 2021/4/23: runtime: 40 ms, memory: 14.6 MB
#

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s1 = haystack
        s2 = needle

        i = 0
        j = 0

        if not s2:
            return 0
        
        if not s1 and s2:
            return -1

        while i < len(s1):
            #print(i, s1[i], j, s2[j])


            if s1[i] == s2[j]:
                i += 1
                j += 1

                if j == len(s2):
                    return i - j

            else:
                i = i - j + 1
                j = 0

            #print('          ', i, j)

        return -1


