from typing import List
import pdb

#
# 2021/4/24: 19 mins, runtime: 48 ms, memory: 15.7 MB
#

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d = False

        i = len(a) - 1
        j = len(b) - 1
        c = '0'
        out = ''
        table = {    # a, b, c ---> c, d
            ('0', '0', '0'): ['0', '0'],
            ('0', '0', '1'): ['0', '1'],
            ('0', '1', '0'): ['0', '1'],
            ('0', '1', '1'): ['1', '0'],
            ('1', '0', '0'): ['0', '1'],
            ('1', '0', '1'): ['1', '0'],
            ('1', '1', '0'): ['1', '0'],
            ('1', '1', '1'): ['1', '1'],
            }

        out = ''
        while True:

            if i == -1:
                v1 = '0'
            else:
                v1 = a[i]
            
            if j == -1:
                v2 = '0'
            else:
                v2 = b[j]    

            if d:
                print('%d, %d, %s, %s, %s' % (i, j, v1, v2, c))
 
            [c, d] = table[(v1, v2, c)]
            if d:
                print('          %s, %s' % (d, c))

            out = d + out

            if i >= 0:
                i -= 1

            if j >= 0:    
                j -= 1           
 
            if i == -1 and j == -1:
                break

        if c == '1':
            out = c + out

        #pdb.set_trace()

        return out