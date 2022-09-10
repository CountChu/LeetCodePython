from typing import List
import pdb


solution_json = {
    "date": "2021/4/24",
    "design": 10,
    "coding": 11,
    "runtime": "716 ms",
    "memory": "14.3 MB"
}

class Solution:
    def lengthOfLongestSubstring(self, s):
        d = False

        out = 0
        n = len(s)
        if d:
            print('i, j, c, h ---> h, out')
        for i in range(n):
            h = {}
            for j in range(i, n):
                c = s[j]
                if d:
                    print('%d, %d, %s, %s' % (i, j, c, [*h]))

                if c not in h:
                    h[c] = j
                    if out < len(h):
                        out = len(h)
                else:
                    h = {}

                if d:
                    print('                  %s, %d' % ([*h], out))

                if h == {}:
                    break

            #pdb.set_trace()

        #pdb.set_trace()
        return out
