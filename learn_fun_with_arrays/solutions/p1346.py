from typing import List
import pdb

#
# 2021/4/28: 5 mins, 11 mins, 52 ms, 14.4 MB
#

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = False
        out = False

        n = len(arr)
        hash = {}
        for i in range(n):
            v = arr[i]
            if v not in hash:
                hash[v] = i

        if d:
            print(hash)

        for i in range(n):
            v = arr[i]
            v2 = 2 * v

            if d:
                print(i, v, v2)            

            if v2 in hash:
                #if True:
                if hash[v2] != i:
                    out = True
                    break

        #pdb.set_trace()
        return out
