#
# https://leetcode.com/problems/group-anagrams/
#
# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different 
# word or phrase, typically using all the original letters exactly once.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/9",
    "design": 0,
    "coding": 7,
    "runtime": "111 ms",
    "fasterThan": "89%",
    "memory": "17.2 MB" 
}

'''
    "eat"  -> 'aet'
    "tea"  -> 'aet'
    "tan"  -> 'ant'
    "ate"
    "nat"
    "bat"
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            ls = list(s)
            ls.sort()
            key = ''.join(ls)
            if key not in h:
                h[key] = []
            h[key].append(s)

        out = []
        for key, ls in h.items():
            out.append(ls)

        return out





