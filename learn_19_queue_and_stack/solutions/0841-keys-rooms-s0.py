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
    "date": "1975/9/4",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

#
#   Official solution.
#   https://leetcode.com/problems/keys-and-rooms/solutions/133880/keys-and-rooms/
#

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:  
            node = stack.pop()
            for nei in rooms[node]: 
                if not seen[nei]: 
                    seen[nei] = True 
                    stack.append(nei) 
        
        return all(seen)





