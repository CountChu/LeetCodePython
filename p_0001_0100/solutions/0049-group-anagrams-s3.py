solution_json = {
    "date": "2023/12/28",
    "design": 0,
    "coding": 4,
    "runtime": "194 ms",
    "fasterThan": "5%",
    "memory": "21.52 MB"
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
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        "eat", "tea", "tan", "ate", "nat", "bat"
    
        "eat" -> ['a', 'e', 't'] - (a, e, t)


'''

def trans(s):
    return tuple(sorted(s))

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            t = trans(s)
            #lg('%s -> %s' % (s, t))
            if not t in h:
                h[t] = []
            h[t].append(s)
        
        out = []
        for t, ls in h.items():
            out.append(ls)

        return out
