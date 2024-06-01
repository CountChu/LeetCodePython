from typing import List
import pdb

solution_json = {
    "date": "2021/4/23",
    "coding": 7,
    "runtime": "40 ms",
    "memory": "15.7 MB"                    
}  

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        debug = False

        n = len(digits)

        c = 1
        for i in reversed(range(n)):
            d = digits[i]
            d2 = d + c

            if debug:
                print(i, d, c, d2)

            if d2 == 10:
                d2 = 0
                c = 1
            else:
                c = 0

            digits[i] = d2

        if c == 1:
            digits.insert(0, c)
        #pdb.set_trace()
        return digits
