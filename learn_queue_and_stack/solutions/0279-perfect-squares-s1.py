from typing import List
import pdb

solution_json = {
    "date": "2021/5/15",
    "design": 9,
    "coding": 13,
    "bug": "Time Limit Exceeded"
} 

class Solution:
    def numSquares(self, n: int) -> int:
        d = False

        nd_ls = []
        v1 = 1
        while True:
            v2 = v1 * v1
            if v2 > n:
                break
            nd_ls.append(v2)
            v1 += 1

        if d:
            print('nd_ls = %s' % nd_ls)

        q = []
        level = 1
        for nd in nd_ls:
            acc = nd
            q.append((nd, level, acc))

        if d:
            print('q = %s' % q)

        table = []
        while True:
            if q == []:
                break

            nd0, l0, acc0 = q.pop(0)
            if d:
                print(nd0, l0, acc0)
            if acc0 == n:
                table.append((l0, acc0))
                break

            for nd1 in nd_ls:
                acc1 = acc0 + nd1
                if acc1 > n:
                    break
                q.append((nd1, l0+1, acc1))

        #pdb.set_trace()

        return table[0][0]
