from typing import List
import pdb

#
# 2021/4/28: 7 mins, 8 mins, 1352 ms, 16.9 MB
#

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        d = False

        v = arr
        n = len(v)
        ls = v[1:n]
        ls.sort(reverse=True)

        if d:
        	print('ls = %s' % ls)

        out = []
        for i in range(1, n):
        	if d:
        		print(i, v[i])

        	out.append(ls[0])
        	ls.remove(v[i])

        out.append(-1)
        return out
