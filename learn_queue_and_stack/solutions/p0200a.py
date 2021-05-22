from typing import List
import pdb

#
# 2021/5/22: 7, 30, 160 ms, 20.2 MB
#

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = False
        g = grid
        v = {}  # visited v[(i, j)] = label or 0

        m = len(g)
        n = len(g[0])
        if d:
            print('m = %d, n = %d' % (m, n))

        ctx = {'label': 0}
        for i in range(m):
            for j in range(n):
                if g[i][j] == '1':
                    if (i, j) not in v:
                        ctx['label'] += 1
                        go(v, g, m, n, i, j, ctx)

        return ctx['label']

def go(v, g, m, n, i, j, ctx):
    d = False

    stack = [(i, j)]
    v[(i, j)] = ctx['label']

    while True:
        if stack == []:
            break

        i, j = stack[-1]
        if d:
            print('(%d, %d)' % (i, j))

        #
        # Go right
        #

        if j+1 <= n-1 and  (i, j+1) not in v and g[i][j+1] == '1':
            stack.append((i, j+1))
            v[(i, j+1)] = ctx['label']

        #
        # Go down
        #

        elif i+1 <= m-1 and (i+1, j) not in v and g[i+1][j] == '1':
            stack.append((i+1, j))
            v[(i+1, j)] = ctx['label']

        #
        # Go left
        #

        elif j-1 >= 0 and (i, j-1) not in v and g[i][j-1] == '1':
            stack.append((i, j-1))
            v[(i, j-1)] = ctx['label']

        #
        # Go up
        #

        elif i-1 >= 0 and (i-1, j) not in v and g[i-1][j] == '1':
            stack.append((i-1, j))
            v[(i-1, j)] = ctx['label']

        else:
            stack.pop()





