#
# https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/31",
    "design": 0,
    "coding": 0,
    "runtime": "80 ms",
    "fasterThan": "18%",
    "memory": "14 MB" 
}

'''
    flower
    flow    ---> flow 


'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = strs[0]
        for i in range(1, len(strs)):
            out = get_common_prefix(out, strs[i])

        return out

def get_common_prefix(str0, str1):
    #print(str0, str1)
    n = min(len(str0), len(str1))
    same = True
    out = ''
    for i in range(n):
        if str0[i] != str1[i]:
            break 
        out += str0[i]

    return out



