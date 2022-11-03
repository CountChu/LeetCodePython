#
# https://leetcode.com/problems/keys-and-rooms/
#
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except 
# for room 0. Your goal is to visit all the rooms. However, 
# you cannot enter a locked room without having its key.
#
# When you visit a room, you may find a set of distinct keys in it. 
# Each key has a number on it, denoting which room it unlocks, 
# and you can take all of them with you to unlock the other rooms.
#
# Given an array rooms where rooms[i] is the set of keys that you can obtain 
# if you visited room i, return true if you can visit all the rooms, 
# or false otherwise.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/30",
    "design": 0,
    "coding": 0,
    "runtime": "114 ms",
    "fasterThan": "70%",
    "memory": "14.6 MB" 
}

'''
     0    1    2   3 
    [1], [2], [3], []

     0      1        2    3
    [1,3], [3,0,1], [2], [0]

     0      1   2    3
    [2,3], [], [2], [1,3]

     0      1      2          3   4
    [1,3], [1,4], [2,3,4,1], [], [4,3,2]    

     0   1    2      3
    [1], [], [0,3], [1]

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        g = {}
        for i, room in enumerate(rooms):
            g[i] = {}
            for key in room:
                #print(i, key)
                g[i][key] = True

        seen = go(g, 0)
        return len(seen) == len(rooms)

def go(g, v0):
    queue = [v0]
    seen = set()
    seen.add(v0)
    while True:
        if queue == []:
            break

        v0 = queue.pop(0)

        for v1 in list(g[v0].keys()):
            if v1 in seen:
                continue 

            queue.append(v1)
            seen.add(v1)

    return seen





