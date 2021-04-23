#
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer 
# range [-2**31, 2**31 - 1], then return 0.
#

import pdb

#
# 2021/4/3: 9 mins, Runtime: 32ms, Memory: 14.3 MB
#

class Solution:
    def reverse(self, x: int) -> int:
    
        #print('x = %d' % x)
        v2 = 0
        s = 1
        if x < 0:
            x = -x
            s = -1            
        while True:
            v1 = x % 10
            x = x // 10
            v2 = v2 * 10 + v1
            #print(v1, x, v2)
            if x == 0:
                break
        v2 = s * v2        

        if not ((-2)**31 <= v2 <= 2**31 - 1):
            v2 = 0
            
        return v2            




        