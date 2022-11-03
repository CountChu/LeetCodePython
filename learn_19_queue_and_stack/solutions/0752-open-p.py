#
# https://leetcode.com/problems/open-the-lock/
#
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
# '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
# The wheels can rotate freely and wrap around: 
# for example we can turn '9' to be '0', or '0' to be '9'. 
# Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any 
# of these codes, the wheels of the lock will stop turning 
# and you will be unable to open it.
#
# Given a target representing the value of the wheels that will unlock the lock, 
# return the minimum total number of turns required to open the lock, or -1 
# if it is impossible.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/14",
    "design": 0,
    "coding": 0,
    "runtime": "4916 ms",
    "fasterThan": "5%",
    "memory": "16.6 MB" 
}

'''
    ["0201", "0101", "0102", "1212", "2002"] 0202
    0000
    0100         1000
    0200         1100
    0201x  0210  1200
           1210  1201
           1201  1202
           1202  0202
           0202

    0000 -> 1000    1000 -> 2000
         -> 0100         -> 1100
         -> 0010         -> 1010
         -> 0001         -> 1001
         -> 9000         -> 0000
         -> 0900         -> 1900
         -> 0090         -> 1090
         -> 0009         -> 1009
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        queue = [('0000', 0)]
        found = False
        seen = set()
        while True:
            if queue == []:
                break

            v0, level = queue.pop(0)
            if v0 == target:
                found = True
                break

            if v0 in seen:
                continue

            if v0 in deadends:
                continue

            seen.add(v0)

            queue.append((rotate(v0, 0, +1), level + 1))
            queue.append((rotate(v0, 1, +1), level + 1))
            queue.append((rotate(v0, 2, +1), level + 1))
            queue.append((rotate(v0, 3, +1), level + 1))
            queue.append((rotate(v0, 0, -1), level + 1))
            queue.append((rotate(v0, 1, -1), level + 1))
            queue.append((rotate(v0, 2, -1), level + 1))
            queue.append((rotate(v0, 3, -1), level + 1))

        if found:
            return level
        else:
            return -1

g_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
g_h = {}
for i, num_s in enumerate(g_nums):
    g_h[num_s] = i

def rotate(v, idx, move):
    global g_h

    num_s = v[idx]
    num = (g_h[num_s] + move) % 10
    out = list(v)
    out[idx] = g_nums[num]
    out = ''.join(out)

    return out







