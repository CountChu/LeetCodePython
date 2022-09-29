from typing import List
import pdb

solution_json = {
   "date": "2021/4/29",
    "design": 5,
    "coding": 4,
    "runtime": "84 ms",
    "memory": "14.8 MB"      
}

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        def swap(out, i, j):
            out[i], out[j] = out[j], out[i]

        d = False

        out = []
        n = len(A)

        j = 0
        for i in range(n):
            if d:
                print(i, A[i])

            out.append(A[i])
            if A[i] % 2 == 0:
                swap(out, i, j)
                #pdb.set_trace()
                j += 1


        #pdb.set_trace()
        return out