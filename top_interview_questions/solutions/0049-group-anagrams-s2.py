solution_json = {
    "date": "2023/12/14",
    "design": 0,
    "coding": 7,
    "runtime": "100 ms",
    "fasterThan": "56%",
    "memory": "19.58 MB"
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
lg = print

'''
    eat tea tan ate nat bat
    aet aet ant aet ant abt 



'''

def gen(s):
    ls = []
    for c in s:
        ls.append(c)

    ls.sort()

    out = ''
    for c in ls:
        out += c

    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            k = gen(s)
            if k not in h:
                h[k] = []

            h[k].append(s)
        
        out = []
        for k, v in h.items():
            out.append(v)

        return out
