# 
# Given a string s, return the longest palindromic substring in s.
#

from typing import List
import pdb

#
# 4/11: 22 mins, Runtime: 100 ms, Memory: 14.8 MB
#

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        f = {}  # f[y][x] = c
        y = 0
        x = 0
        state = 'init'
        
        for i in range(n):
            if state == 'init':
                state = 'down'
            elif state == 'down' and y+1 == numRows:
                state = 'up'
            elif state == 'down' and y+1 != numRows:
                state = 'down'
            elif state == 'up' and y == 0:
                state = 'down'
            elif state == 'up' and y != 0:
                state = 'up'
            else:
                assert False
        
            #print(i, x, y, state)
            if y not in f:
                f[y] = {}
            if x not in f[y]:
                f[y][x] = {}
            f[y][x] = s[i]
            
            if state == 'down':
                y += 1
            elif state == 'up':
                y -= 1
                x += 1
            else:
                assert False
            
        out = ''    
        for y in f:
            for x in f[y]:
                c = f[y][x]
                out += c
        
        return out