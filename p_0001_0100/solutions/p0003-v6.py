from typing import List
import pdb

#
# 2021/4/24: 28 mins, runtime: 80 ms, memory 15.5 MB
#

class Solution:
    def lengthOfLongestSubstring(self, s):
        d = False

        if s == '':
            return 0

        i = 0
        j = 0

        def w(i, j):
            return s[i:j+1]

        out = 0
        while True:

            if d:
                print('%d, %d, %s' % (i, j, w(i, j)))

            idx = w(i, j-1).find(s[j])
            if idx != -1:
                i = i + idx + 1    
                if d:            
                    print('          %d, %d, %s' % (i, j, w(i, j)))

            if out < len(w(i, j)):
                out = len(w(i, j))


            j += 1
            if j == len(s):
                break

        '''
        if out < len(w(i, j)):
            out = len(w(i, j))
        '''

        #pdb.set_trace()
        return out

