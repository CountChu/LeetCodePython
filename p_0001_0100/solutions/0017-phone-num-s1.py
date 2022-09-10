from typing import List
import pdb

solution_json = {
    "date": "2021/4/17",
    "coding": 15,
    "runtime": "40 ms",
    "memory": "15.5 MB"          
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        debug = False

        if digits == '':
            return []

        if debug:
            print('digits = %s' % digits)

        d_lts = {   # digit to letters
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }

        n = len(digits)

        comb = d_lts[digits[0]]
        if debug:
            print('comb = %s' % comb)

        for i in range(1, n):
            comb = self.get_comb(comb, d_lts[digits[i]])

        return comb

    def get_comb(self, comb0, comb1):
        out = []
        for c0 in comb0:
            for c1 in comb1:
                out.append(c0+c1)
        return out

