from typing import List
import pdb

solution_json = {
    "date": "2021/6/29",
    "design": 0,
    "coding": 35,
    "runtime": "80 ms",
    "memory": "15.7 MB"
}   

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        d = False

        m = len(image)
        n = len(image[0])
        color = image[sr][sc]

        q = []
        visited = {}  # visited[(y, x)] = True

        pos = (sr, sc)
        visited[pos] = True
        q.append(pos)
        
        while True:
            if q == []:
                break
            if d:
                print('q = %s' % q)
                print('    visited = %s' % visited)

            first = q.pop(0)
            if d:
                print('    first   =', first)
            image[first[0]][first[1]] = newColor

            pos_ls = get_neighbor(image, m, n, color, first, visited)
            for pos in pos_ls:
                visited[pos] = True
                q.append(pos)

            if d:
                print('    pos_ls    = %s' % pos_ls)

            #pdb.set_trace()
        return image

def get_neighbor(image, m, n, color, pos, visited):
    y, x = pos
    out_ls = []

    #
    # Move left
    #

    if x - 1 >= 0:
        pos = (y, x-1)
        if not pos in visited:
            if image[pos[0]][pos[1]] == color:
                out_ls.append(pos)

    #
    # Move top
    #

    if y - 1 >= 0:
        pos = (y-1, x)
        if not pos in visited:
            if image[pos[0]][pos[1]] == color:  
                out_ls.append(pos)

    #
    # Move right
    #

    if x + 1 <= n - 1:
        pos = (y, x+1)
        if not pos in visited:
            if image[pos[0]][pos[1]] == color:  
                out_ls.append(pos)

    #
    # Move bottom
    #

    if y + 1 <= m - 1:
        pos = (y+1, x)
        if not pos in visited:
            if image[pos[0]][pos[1]] == color:  
                out_ls.append(pos)

    return out_ls
