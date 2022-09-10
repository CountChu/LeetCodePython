# 
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.
# 

from typing import List
import pdb

solution_json = {
    "date": "2021/3/25",
    "runtime": "76 ms",
    "memory": "14.7 MB"
}

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
            
        for i in range(len(haystack)):
            line = ''
            line += 'i = %d, ' % i
            s1 = haystack[i:(i+len(needle))]
            line += 's1 = %s, ' % s1
            if s1 == needle:
                return i
            #print(line)

        return -1
