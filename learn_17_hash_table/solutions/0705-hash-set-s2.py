#
# https://leetcode.com/problems/design-hashset/
#
# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
#   void add(key) 
#       Inserts the value key into the HashSet.
#   bool contains(key)
#       Returns whether the value key exists in the HashSet or not.
#   void remove(key) 
#       Removes the value key in the HashSet. If key does not exist in the HashSet, 
#       do nothing.
#
#
# Example 1:
#       Input: 
#           [
#               "MyHashSet", "add", "add", "contains", "contains", 
#               "add", "contains", "remove", "contains"
#           ],
#           [
#               [], [1], [2], [1], [3], 
#               [2], [2], [2], [2]
#           ]
#
#       Output: 
#           [
#               null, null, null, true, false, 
#               null, true, null, false
#           ] 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/10",
    "design": 0,
    "coding": 0,
    "runtime": "200 ms",
    "fasterThan": "91%",
    "memory": "19.8 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

#
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)        
#

class MyHashSet:
    def __init__(self):
        self.n = 10000
        self.b = [[] for i in range(self.n)] # bucket
        pass

    def dump(self):
        for y, ls in enumerate(self.b):
            for x, v in enumerate(ls):
                print('%d: %d: %s' % (x, y, v))

    def add(self, key: int) -> None:
        y, found, x = get_idx(self.n, self.b, key)

        if not found:
            if x == -1:
                self.b[y].append(key)
            else:
                self.b[y][x] = key        

    def remove(self, key: int) -> None:
        y, found, x = get_idx(self.n, self.b, key)
        if not found:
            return

        self.b[y][x] = None

    def contains(self, key: int) -> bool:
        y, found, x = get_idx(self.n, self.b, key)
        return found

def get_idx(n, b, key):
    y = key % n
    found = False
    x = -1
    x2 = -1
    for i, v in enumerate(b[y]):
        if v == None:
            if x2 == -1:
                x2 = i

        if key == v:
            found = True
            x = i

    if found:
        return y, found, x 
    else:
        return y, found, x2