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
    "date": "2022/9/20",
    "design": 0,
    "coding": 0,
    "runtime": "860 ms",
    "fasterThan": "23%",
    "memory": "17.3 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findNumbers(self, nums: List[int]) -> int:
        return 0

#
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
#

class MyHashMap:
    def __init__(self):
        n = 100 

        #
        # b is bucket.
        # idx = cal_idx(key)
        # b[idx] = [(key, value)]
        #

        self.b = [[] for _ in range(n)]
        pass

    def __str__(self):
        return '%s' % self.b

    def dump(self):
        print(str(self))        

    def cal_idx(self, key):
        idx = key % len(self.b)
        return idx 

    def find(self, key):
        i = self.cal_idx(key)
        found_j = -1
        for j, (k, v) in enumerate(self.b[i]):
            if k == key:
                found_j = j 
                break 
        return i, found_j        

    def put(self, key: int, value: int) -> None:
        i, j = self.find(key)

        if j == -1:
            self.b[i].append((key, value))
        else:
            self.b[i][j] = (key, value)

    def get(self, key: int) -> int:
        i, j = self.find(key)
        if j == -1:
            return -1 
        else:
            return self.b[i][j][1]

    def remove(self, key: int) -> None:
        i, j = self.find(key)

        if j == -1:
            return 
        else:
            del self.b[i][j]
        