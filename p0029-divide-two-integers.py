from typing import List
import pdb

#
# 2021/4/23: 8 mins, Time Limit Exceeded.
#

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = False

        out = 0
        a = dividend
        b = divisor
        
        s = False
        if a < 0 and b < 0:
            a = -a
            b = -b
        elif a > 0 and b < 0:
            b = -b
            s = True
        elif a < 0 and b > 0:
            a = -a
            s = True

        while True:
            if d:
                print(a, out)
            if a >= b:
                a = a - b
                out += 1
            else:
                break

        if s:
            out = -out

        #pdb.set_trace()
        return out
