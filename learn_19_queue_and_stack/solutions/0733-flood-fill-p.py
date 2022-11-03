#
# https://leetcode.com/problems/flood-fill/
#
# An image is represented by an m x n integer grid image where image[i][j] 
# represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color. 
# You should perform a flood fill on the image starting 
# from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels 
# connected 4-directionally to the starting pixel of the same color 
# as the starting pixel, plus any pixels connected 4-directionally 
# to those pixels (also with the same color), and so on. Replace the color 
# of all of the aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/29",
    "design": 0,
    "coding": 0,
    "runtime": "197 ms",
    "fasterThan": "10%",
    "memory": "14 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])
        seen = set()
        v = image[sr][sc]
        go(image, h, w, sr, sc, v, seen)
        
        for y, x in seen:
            image[y][x] = color

        return image

def go(image, h, w, y, x, v, seen):
    if (y, x) in seen:
        return
    if image[y][x] != v:
        return

    #print(y, x)
    seen.add((y, x))

    if can_move_left(h, w, y, x):
        go(image, h, w, y, x-1, v, seen)
    
    if can_move_right(h, w, y, x):
        go(image, h, w, y, x+1, v, seen)

    if can_move_up(h, w, y, x):
        go(image, h, w, y-1, x, v, seen)        
    
    if can_move_down(h, w, y, x):
        go(image, h, w, y+1, x, v, seen)
    

def can_move_left(h, w, y, x):
    return x >= 1

def can_move_right(h, w, y, x):
    return x <= w - 2

def can_move_up(h, w, y, x):
    return y >= 1

def can_move_down(h, w, y, x):
    return y <= h - 2




      
