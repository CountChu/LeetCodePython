#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#

from typing import List
import pdb

solution_json = {
    "date": "2022/8/28",
    "coding": 0,
    "runtime": "70 ms",
    "fasterThan": "88%",
    "memory": "14.1 MB"
}  

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        j = 0
        max_len = 0
        h = {}
        h[s[j]] = j
        for i in range(1, len(s)):
            if s[i] in h:
                pos = h[s[i]]
                if pos >= j:
                    j = pos + 1
            h[s[i]] = i 
            #print(j, i, s[j:i], s[i], h)
            max_len = max(max_len, i-j+1)

        return max_len