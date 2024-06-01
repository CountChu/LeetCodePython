solution_json = {
    "date": "2024/5/27",
    "design": 0,
    "coding": 22,
    "runtime": "35 ms",
    "fasterThan": "75%",
    "memory": "16 MB"
}

#
# https://leetcode.com/problems/longest-common-prefix/
#
# Easy.
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    ["flower", "flow", "flight"], "fl"

           0 1 2 3 4 5  x
        0: f l o w e r
        1: f l o w 
        2: f l i g h t
               X

        h = 3 

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        h = len(strs)

        out = ''
        x = 0
        stop = False
        while True:
            c = None
            for y in range(h):
                if x >= len(strs[y]):
                    stop = True
                    break

                if c == None:
                    c = strs[y][x]
                else:
                    if c != strs[y][x]:
                        stop = True
                        break 

            if stop:
                break
            #lg(i, c)                
            out += c

            x += 1
        
        return out
