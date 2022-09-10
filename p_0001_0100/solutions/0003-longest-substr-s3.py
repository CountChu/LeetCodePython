# 
# Given a string s, find the length of the longest substring without repeating characters.
# 

from typing import List
import pdb


solution_json = {
    "date": "2021/4/10",
    "coding": 29,
    "runtime": "508 ms",
    "memory": "17.5 MB"
}

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1

        hash = {} # hash[idx] = idx2
        max = 0
        for i in range(n - 1):
            hash[i] = i
            for j in range(i + 1, n):
                if s[j] in s[i:j]:
                    break
                else:
                    hash[i] = j
            sub_str = s[i:(hash[i]+1)]        
            if max < len(sub_str):
                max = len(sub_str)
            #print(i, hash[i], sub_str)
        return max
