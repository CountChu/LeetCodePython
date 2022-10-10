#
# https://leetcode.com/problems/design-hashmap/
#
# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#   MyHashMap() 
#       initializes the object with an empty map.
#   void put(int key, int value) 
#       inserts a (key, value) pair into the HashMap. If the key already exists 
#       in the map, update the corresponding value.
#   int get(int key) 
#       returns the value to which the specified key is mapped, or -1 
#       if this map contains no mapping for the key.
#   void remove(key) 
#       removes the key and its corresponding value if the map contains the mapping 
#       for the key.
#
# Example 1:
#       Input
#           ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
#           [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
#       Output
#           [null, null, null, 1, -1, null, 1, null, -1]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/10",
    "design": 0,
    "coding": 0,
    "runtime": "1644 ms",
    "fasterThan": "16%%",
    "memory": "18.3 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

#
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
#

class MyHashMap:
    def __init__(self):
        self.n = 10000
        self.b = [[] for i in range(self.n)] # bucket, b[y][x] = (key, value)

    def dump(self):
        for y, ls in enumerate(self.b):
            for x, pair in enumerate(ls):
                if pair != None:
                    print('%d: %d: %s' % (y, x, pair))

    def put(self, key: int, value: int) -> None:
        y, found, x = find(self.b, self.n, key)
        if found:
            self.b[y][x] = (key, value)
        else:
            self.b[y].append((key, value))

    def get(self, key: int) -> int:
        y, found, x = find(self.b, self.n, key)
        if not found:
            return -1

        _, value = self.b[y][x]
        return value

    def remove(self, key: int) -> None:
        y, found, x = find(self.b, self.n, key)
        if not found:
            return  

        self.b[y][x] = None


def find(b, n, key):
    y = key % n
    found = False
    x = -1
    x_none = -1
    for i, pair in enumerate(b[y]):
        if pair == None:
            if x_none == -1:
                x_none = i
        else:
            if pair[0] == key:
                found = True
                x = i   
                break

    if found:
        return y, found, x
    else:
        return y, found, x_none



