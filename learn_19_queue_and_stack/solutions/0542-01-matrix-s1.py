from typing import List
import pdb

solution_json = {
    "date": "2021/7/1",
    "design": 16,
    "coding": 32,
    "bug": "Time Limit Exceeded"
}    

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        d = False

        out = mat.copy()

        m = len(mat)
        n = len(mat[0])
        
        #pos = (1, 3) # pos = (y, x)
        #dist = get_distance(mat, m, n, pos)

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dist = get_distance(mat, m, n, (i, j))
                    out[i][j] = dist

        return out

def get_distance(mat, m, n, p0):
    d = False

    min_dist = m + n - 1
    for i in range(m):
        for j in range(n):
            p = (i, j)
            if p == p0:
                continue

            if d:
                print(p)   

            if mat[i][j] == 0:
                dist = cal_dist(p0, p)
                min_dist = min(min_dist, dist)
    
    return min_dist

def cal_dist(p0, p1):
    return abs(p0[0]-p1[0]) + abs(p0[1]-p1[1])
