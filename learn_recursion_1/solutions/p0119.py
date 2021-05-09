from typing import List
import pdb

#
# 2021/5/9: 18, 9, 44 ms, 15.7 MB
#

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        h = {}
        row = getRow(rowIndex, h)
        return row

def getRow(i, h):
    d = False

    if i == 0:
        return [1]   
    if i == 1:
        return [1, 1]

    center = build_center(getRow(i-1, h), h)
    row = [1] + center + [1]    
    return row

def build_center(row, h):
    d = False
    if d:
        print('row = %s' % row)
    
    center = []
    n = len(row)
    for i in range(n-1):
        v0 = row[i]
        v1 = row[i+1]
        if (v0, v1) not in h:
            h[(v0, v1)] = v0 + v1
        v = h[(v0, v1)]
        center.append(v)

    if d:
        print('center = %s' % center)

    return center       
