from typing import List
import pdb

solution_json = {
    "date": "2021/6/13",
    "design": 8,
    "coding": 27,
    "bug": "Time Limit Exceeded"
}   

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = False

        v = nums
        n = len(v)
        k = {}      # k[0] = [+, -], k[1] = [++, +-, -+, --]
        h = {}      # h[+] = v[0], h[+-] = h[+] - v[1]
        for i in range(n):
            if i == 0:
                k[0] = ['+', '-']
            else:
                k[i] = build(k[i-1])

            if d:
                print('k[%d] = %s' % (i, k[i]))
                
            for simbols in k[i]:
                assert simbols not in h
                last_s = simbols[-1]
                if last_s == '+':
                    if i == 0:
                        h[simbols] = 0 + v[i]
                    else:
                        h[simbols] = h[simbols[:-1]] + v[i]
                elif last_s == '-':
                    if i == 0:
                        h[simbols] = 0 - v[i]
                    else:
                        h[simbols] = h[simbols[:-1]] - v[i]
                else:
                    assert False, last_s

        out = 0
        for simbols in k[n-1]:
            if h[simbols] == target:
                out += 1

        #pdb.set_trace()
        return out

def build(k0):
    k1 = []
    for simbols in k0:
        k1.append(simbols+'+')
        k1.append(simbols+'-')
    return k1                    
