#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/4",
    "design": 0,    
    "coding": 9,
    "runtime": "5575 ms",
    "fasterThan": "5%",    
    "memory": "14.1 MB"
}  


'''
        0 1 2 3 4 5 6 7
        a b c a b c b b
      0 a b c
      1   b c a 
      2     c a b
      3       a b c
      4         b c
      5           c b
      6             b
      7               b

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        out = 0
        for i, c in enumerate(s):
            idx_ls = handle(i, c, h)
            for idx in idx_ls:
                out = max(out, len(h[idx]))
                del h[idx]
        
        for i in h:
            out = max(out, len(h[i]))

        return out

def handle(idx, c, h):
    out_ls = []
    for i in h:
        if c in h[i]:
            out_ls.append(i)
        else:
            h[i].append(c)

    h[idx] = [c]
    return out_ls

