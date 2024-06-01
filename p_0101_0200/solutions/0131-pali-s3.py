solution_json = {
    "date": "2024/1/5",
    "design": 0,
    "coding": 23,
    "runtime": "447 ms",
    "fasterThan": "99%",
    "memory": "31.16 MB"
}

#
# https://leetcode.com/problems/palindrome-partitioning/
#
# Given a string s, partition s such that every substring of the partition 
# is a palindrome. Return all possible palindrome partitioning of s.
#

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

        (aab)
            a, (ab)
                ab    -> [a, ab] 
                a, b  -> [a, a, b] 
            aa, (b)
                b     -> [aa, b]
            aab,      -> [aab]     x

'''

def is_pali(s):
    n = len(s)
    i = 0
    j = n - 1
    out = True
    while True:
        if i > j:
            break

        if s[i] != s[j]:
            out = False
            break
        i += 1
        j -= 1

    return out

def go(s, level, path, out, dp):
    #lg('%s(%s)' % ('    '*level, s))
    for i in range(1, len(s)+1):
        s0 = s[:i]
        if s0 not in dp:
            flag = is_pali(s0)
            dp[s0] = flag

        if not dp[s0]:
            continue

        path.append(s0)

        s1 = s[i:]
        #lg('%s%s, %s' % ('    '*(level+1), s0, s1))
        
        if s1 != '':
            go(s1, level+1, path, out, dp)
        else:
            #lg('%spath = %s' % ('    '*(level+1), path))
            out.append(path.copy())

        path.pop()

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def partition(self, s: str) -> List[List[str]]:
        level = 0
        path = []
        out = []
        dp = {}
        go(s, level, path, out, dp)
        return out




