from typing import List
import pdb

#
# 2021/4/24: 7 mins, 17 mins, runtime: 1648 ms, memory 17.7 MB
#

class Solution:
    def mySqrt(self, x: int) -> int:
        d = False

        if x == 0:
            return 0
        elif x == 2:
            return 1
        elif x == 1:
            return 1

        table = []

        
        i = 1
        v1 = 1
        while True:
            v1 = v1 * 2
            v2 = v1 * v1
            row = (v1, v2)
            table.append(row)
            if v2 >= x:
                break

        if d:
            for row in table:
                print(row)

        if len(table) == 1:
            r0 = table[0]
            if r0[1] > x:
                return r0[0] - 1
            else:
                return r0[0]

        table = table[-2:]
        r0 = table[0]
        r1 = table[1]
        
        table = []
        for v1 in range(r0[0], r1[0] + 1):
            v2 = v1 * v1
            if d:
                print (v1, v2)

            table.append([v1, v2]) 
            if v2 >= x:
                break

        row = table[-1] 
        if row[1] == x:
            return row[0]
        else:
            row = table[-2]
            return row[0]

