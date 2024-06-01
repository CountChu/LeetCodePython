solution_json = {
    "date": "2024/1/15",
    "design": 0,
    "coding": 3,
    "runtime": "78 ms",
    "fasterThan": "98%",
    "memory": "21 MB"
}

#
# https://leetcode.com/problems/group-anagrams/
#
# Medium.
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
lg = print

'''
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        ["eat", "tea", "tan", "ate", "nat", "bat"]

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}
        for s in strs:
            t = tuple(sorted(list(s)))
            if not t in h:
                h[t] = []

            h[t].append(s)
        #lg(h)

        out = []
        for t, s_ls in h.items():
            out.append(s_ls)

        return out

