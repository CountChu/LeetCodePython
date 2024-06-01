solution_json = {
    "date": "2024/1/12",
    "design": 0,
    "coding": 0,
    "runtime": "453 ms",
    "fasterThan": "96%",
    "memory": "32.94 MB"
}

#
# https://leetcode.com/problems/palindrome-partitioning/
#
# Medium.
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
            a, (ab)         is_pali(a)
                a, (b)      is_pali(a)
                    b       is_pali(b)
                ab
            aa, (b)         is_pali(aa)
                b           is_pali(b)
            aab

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

def go(s, level, path, out):
    #lg('%s[%s]' % ('    '*level, s))

    if len(s) == 0:
        out.append(path.copy())

    if len(s) == 1:
        path.append(s)
        #lg('%spath = %s' % ('    '*level, path))
        out.append(path.copy())
        path.pop()
        return

    for i in range(len(s)):
        s0 = s[0:i+1]
        s1 = s[i+1:]
        #lg('%s%s, %s' % ('    '*level, s0, s1))
        if not is_pali(s0):
            #lg('%sSkip it.' % ('    '*level))
            continue

        path.append(s0)
        go(s1, level+1, path, out)
        path.pop()

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def partition(self, s: str) -> List[List[str]]:
        level = 0
        path = []
        out = []
        go(s, level, path, out)
        return out




