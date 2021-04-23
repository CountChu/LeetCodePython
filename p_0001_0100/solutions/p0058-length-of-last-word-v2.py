from typing import List
import pdb

#
# 2021/4/23: 10 ms, runtime: 32 ms, memory: 14.3 MB
#

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d = False

        pre_m = None
        m = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            if d:
                print(i, c)

            if c == ' ':
                if m != 0:
                    pre_m = m
                m = 0
            else:
                m += 1

        if m == 0:
            if pre_m == None:
                m = 0
            else:
                m = pre_m
        #pdb.set_trace()
        return m