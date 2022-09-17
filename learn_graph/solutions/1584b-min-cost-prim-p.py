#
# https://leetcode.com/problems/min-cost-to-connect-all-points/
#
# You are given an array points representing integer coordinates of some points 
# on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan 
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute 
# value of val.
#
# Return the minimum cost to make all points connected. All points are connected 
# if there is exactly one simple path between any two points.
#
# Example 1:
#       Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
#       Output: 20
#
# Example 2: 
#       Input: points = [[3,12],[-2,5],[-4,1]]
#       Output: 18
#
# Please implement it with Prim's algorithm.
#  

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/16",
    "design": 0,
    "coding": 0,
    "bug": "Time Limit Exceeded"
}

def get_m_dist(v0, v1):
    x0, y0 = v0
    x1, y1 = v1 
    return abs(x0 - x1) + abs(y0 - y1)

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v_nums = len(points)
        e_ls = []
        for i in range(v_nums - 1):
            for j in range(i + 1, v_nums):
                v0 = points[i]
                v1 = points[j]
                d = get_m_dist(v0, v1)
                e_ls.append((i, j, d))
        #print('e_ls = %s' % e_ls)
        
        seen = []
        unseen = [i for i in range(v_nums)]

        out = 0
        v = unseen.pop(0)
        seen.append(v)        
        #print('seen = %s' % seen)

        while True:
            #print('-------------')
            if unseen == []:
                break

            idx = -1
            min_d = -1    
            for i, e in enumerate(e_ls):
                v0, v1, d = e
                if (v0 in seen and v1 not in seen) or (v1 in seen and v0 not in seen):
                    #print('check %s' % str(e))
                    if min_d == -1: 
                        min_d = d
                        idx = i 
                    elif min_d > d:
                        min_d = d
                        idx = i   
            
            e = e_ls.pop(idx)
            #print('e_ls = %s' % e_ls)
            #print('e = %s' % str(e))
            v0, v1, d = e
            if v0 in unseen:
                unseen.remove(v0)
                seen.append(v0)
            elif v1 in unseen:
                unseen.remove(v1)
                seen.append(v1)
            else:
                #print('It makes cycle. e = %s' % str(e))
                continue

            out += d
            #print('seen = %s' % seen)
            #print('unseen = %s' % unseen)
            #print('out = %d' % out)
        
        return out

    
