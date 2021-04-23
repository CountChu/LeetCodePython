import pdb

#
# 3/23: Runtime: 64 ms, Memory: 14.3 MB
#

class Solution:
    def romanToInt(self, s: str) -> int:
        c_v = {             # char-value dict
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
        out = 0
        last_v = None
        for c in s:
            if c not in c_v:
                return 0

            v = c_v[c]
            if last_v != None:
                if last_v < v:
                    out -= last_v
                    out += (v - last_v)
                else:
                    out += v
                print('c = %s, v = %d, out = %d, last_v = %d' % (c, v, out, last_v))
            else:    
                out += v
                print('c = %s, v = %d, out = %d' % (c, v, out))

            last_v = v

        return out