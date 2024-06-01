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
    "date": "2023/11/27",
    "design": 0,
    "coding": 0,
    "runtime": "106 ms",
    "fasterThan": "36%",
    "memory": "19.78 MB" 
}


'''
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    h[aet] = [eat, tea, ate]
    h[ant] = [tan, nat]
    h[abt] = bat
'''

def gen_key(s):
    ls = list(s)
    ls.sort()
    return str(ls)


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            k = gen_key(s)
            if k not in h:
                h[k] = []
            h[k].append(s)

        out = []
        for k, v in h.items():
            out.append(v)

        return out


