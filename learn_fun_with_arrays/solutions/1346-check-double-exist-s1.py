from typing import List
import pdb

solution_json = {
    "date": "2021/4/28",
    "design": 5,
    "coding": 11,
    "runtime": "52 ms",
    "memory": "14.4 MB" 
}

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
