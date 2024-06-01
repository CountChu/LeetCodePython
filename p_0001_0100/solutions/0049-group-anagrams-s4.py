solution_json = {
    "date": "2024/1/9",
    "design": 0,
    "coding": 6,
    "runtime": "83 ms",
    "fasterThan": "92%",
    "memory": "21.33 MB"
}

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
#lg = print

'''
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        ["eat", "tea", "tan", "ate", "nat", "bat"]

'''

def build_touple(s):
    return tuple(sorted(s))

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        h = {}

        for i in range(n):
            s = strs[i]
            t = build_touple(s)
            if t not in h:
                h[t] = []

            h[t].append(s)

        out = []
        for t, ls in h.items():
            out.append(ls)

        return out

