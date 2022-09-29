from typing import List
import pdb


solution_json = {
    "date": "2021/4/28",
    "design": 5,
    "coding": 13,
    "runtime": "232 ms",
    "memory": "16.7 MB"   
}

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        d = False

        n = len(arr)
        arr2 = []
        for i in range(1, n):
            v0 = arr[i-1]
            v1 = arr[i]
            arr2.append(v1 - v0)

        if d:
            print('arr2 = %s' % arr2)

        s = 'init'
        for i in range(n - 1):
            v = arr2[i]
            if s == 'init':
                if v == 0:
                    s = '0'
                elif v < 0:
                    s = 'error'
                elif v > 0:
                    s = '+1'
                else:
                    s = 'error'
            elif s == '0':
                if v == '0':
                    s = '0'
                elif v > 0:
                    s = '+1'
                else:
                    s = 'error'
            elif s == '+1':
                if v == 0:
                    s = 'error'
                elif v > 0:
                    s = '+1'
                elif v < 0:
                    s = '-1'
                else:
                    s = 'error'
            elif s == '-1':
                if v == 0:
                    s = '0'
                elif v < 0:
                    s = '-1'
                else:
                    s = 'error'
            elif s == 'error':
                s = 'error'

            if d:
                print(i, v, s)

            if s == 'error':
                break
        
        #pdb.set_trace()
        return s == '-1'