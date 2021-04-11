# 
# Given a string s, return the longest palindromic substring in s.
#

from typing import List
import pdb

#
# 3/29: Runtime: 496 ms, Memory: 14.4 MB
#

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #print('s = %s, numRows = %d' % (s, numRows))
    
        if numRows == 1:
            return s
    
        x = 0
        y = -1
        down = True
        hash = {}
        for i in range(len(s)):
            line = ''
            if down:
                y += 1
            else:
                y -= 1
                x += 1
            hash[(x, y)] = s[i]


            line += '%5s, ' % down
            line += '%3d, %3d, ' % (x, y)
            
            if down:
                if y == numRows - 1:
                    down = False
                
            else:
                if y == 0:
                    down = True
            
            #print(line)
        max_y = numRows - 1
        max_x = x
        out = ''
        for y in range(max_y+1):
            for x in range(max_x+1):
                if (x, y) in hash:
                        out += hash[(x, y)]
        #pdb.set_trace()
        return out