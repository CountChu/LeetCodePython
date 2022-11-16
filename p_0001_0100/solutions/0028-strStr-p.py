#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#
# Given two strings needle and haystack, return the index of the first occurrence 
# of needle in haystack, or -1 if needle is not part of haystack.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/6",
    "design": 0,
    "coding": 0,
    "runtime": "63 ms",
    "fasterThan": "28%",
    "memory": "13.9 MB" 
}

'''
    0 1 2 3 4 5 6 7 8 9 10  <- i
    m i s s i s s i p p i

      0 1 2 3 4  <- j
      i s s i p
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == '' and needle == '':
            return 0

        if len(haystack) < len(needle):
            return -1

        i = 0 
        j = 0 

        while True:
            if i >= len(haystack):
                break

            if haystack[i] != needle[0]:
                i += 1
            else:
                flag = check(haystack, i, needle)
                if flag:
                    return i
                else:
                    i += 1

        return -1

def check(s0, i, s1):
    #print(s0, i, s1)
    j = 0
    while True:
        if i >= len(s0):
            break

        if j >= len(s1):
            break

        if s0[i] != s1[j]:
            return False

        i += 1
        j += 1

    if j == len(s1):
        return True
    else:
        return False
   
